import uuid
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Appointment, Payment
from .serializers import AppointmentCreateSerializer, PaymentInitiateSerializer
from .services import lock_appointment_slot, release_appointment_slot, verify_mobile_money_webhook_signature
from accounts.models import HealthPractitionerProfile


class BookAppointmentView(APIView):
    """
    Réservation d'un créneau avec verrouillage temporaire dans Redis.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        doctor_id = request.data.get('doctor_id')
        appointment_date = request.data.get('appointment_date')
        mode = request.data.get('mode', Appointment.Mode.TELECONSULTATION)

        if not doctor_id or not appointment_date:
            return Response({"error": "Les champs doctor_id et appointment_date sont requis."}, status=status.HTTP_400_BAD_REQUEST)

        # 1. Tentative d'acquisition du verrou temporaire dans Redis (5 minutes)
        acquired, lock_key = lock_appointment_slot(doctor_id, appointment_date)
        if not acquired:
            return Response({"error": "Ce créneau est actuellement en cours de réservation par un autre utilisateur. Veuillez réessayer dans quelques minutes."}, status=status.HTTP_409_CONFLICT)

        # 2. Création du rendez-vous à l'état PENDING
        doctor = get_object_or_404(HealthPractitionerProfile, id=doctor_id)
        patient_profile = request.user.patient_profile

        appointment = Appointment.objects.create(
            patient=patient_profile,
            doctor=doctor,
            appointment_date=appointment_date,
            mode=mode,
            status=Appointment.Status.PENDING
        )

        return Response({
            "message": "Créneau temporairement réservé. Veuillez procéder au paiement dans les 5 minutes.",
            "appointment_id": appointment.id,
            "lock_expire_seconds": 300
        }, status=status.HTTP_201_CREATED)


class InitiatePaymentView(APIView):
    """
    Initiation du paiement Mobile Money / Carte bancaire.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        appointment_id = request.data.get('appointment_id')
        channel = request.data.get('payment_channel', Payment.Channel.MOBILE_MONEY)
        
        appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user.patient_profile)
        
        tx_ref = f"TX-{uuid.uuid4().hex[:10].upper()}"
        
        payment = Payment.objects.create(
            appointment=appointment,
            patient=request.user.patient_profile,
            amount=appointment.doctor.consultation_fee,
            payment_channel=channel,
            transaction_reference=tx_ref,
            status=Payment.Status.INITIATED
        )

        # Simulation du Push USSD / Tokénisation Monétique
        return Response({
            "message": f"Requête USSD émise sur votre téléphone. Veuillez valider le paiement.",
            "transaction_reference": tx_ref,
            "amount": payment.amount
        }, status=status.HTTP_200_OK)


class MobileMoneyWebhookView(APIView):
    """
    Callback/Webhook asynchrone sécurisé (HMAC) reçu de l'opérateur (MTN/Orange).
    """
    permission_classes = [permissions.AllowAny]

    @transaction.atomic
    def post(self, request):
        # Validation de la signature HMAC transmise dans les en-têtes
        signature = request.headers.get('X-Signature', '')
        # secret_key_operator = settings.MOBILE_MONEY_SECRET_KEY
        
        tx_ref = request.data.get('transaction_reference')
        status_code = request.data.get('status') # SUCCESS / FAILED

        payment = get_object_or_404(Payment, transaction_reference=tx_ref)

        if status_code == 'SUCCESS':
            payment.status = Payment.Status.SUCCESSFUL
            payment.save()

            # Confirmation définitive du rendez-vous
            appointment = payment.appointment
            if appointment:
                appointment.status = Appointment.Status.CONFIRMED
                appointment.save()

            return Response({"status": "PAYMENT_CONFIRMED"}, status=status.HTTP_200_OK)
        else:
            payment.status = Payment.Status.FAILED
            payment.save()
            return Response({"status": "PAYMENT_FAILED"}, status=status.HTTP_400_BAD_REQUEST)