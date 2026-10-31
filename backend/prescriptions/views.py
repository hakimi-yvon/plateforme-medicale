from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Prescription, PharmacyInventory
from .serializers import PrescriptionCreateSerializer, PharmacyInventorySerializer


class CreatePrescriptionView(generics.CreateAPIView):
    """Permet à un médecin d'émettre une ordonnance signée."""
    serializer_class = PrescriptionCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != 'DOCTOR':
            return Response({"error": "Seuls les médecins peuvent émettre une ordonnance."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()


class VerifyAndDispensePrescriptionView(APIView):
    """
    Permet à un pharmacien de vérifier l'authenticité d'une ordonnance
    et d'effectuer la délivrance avec mise à jour du stock (FEFO).
    """
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request, qr_code_token):
        if request.user.role != 'PHARMACIST':
            return Response({"error": "Accès réservé aux pharmaciens."}, status=status.HTTP_403_FORBIDDEN)

        prescription = get_object_or_404(Prescription, qr_code_token=qr_code_token)

        if prescription.status == Prescription.Status.DISPENSED:
            return Response({"error": "Cette ordonnance a déjà été entièrement délivrée."}, status=status.HTTP_400_BAD_REQUEST)

        # Mise à jour des lignes de prescription et décrémentation des stocks officinaux (FEFO)
        for item in prescription.items.all():
            quantity_needed = item.quantity_prescribed - item.quantity_dispensed
            
            # Recherche des stocks disponibles ordonnés par date de péremption (FEFO)
            inventories = PharmacyInventory.objects.filter(
                medication_name__iexact=item.medication_name,
                stock_quantity__gt=0
            ).order_by('expiration_date')

            for inv in inventories:
                if quantity_needed <= 0:
                    break
                
                if inv.stock_quantity >= quantity_needed:
                    inv.stock_quantity -= quantity_needed
                    item.quantity_dispensed += quantity_needed
                    quantity_needed = 0
                else:
                    quantity_needed -= inv.stock_quantity
                    item.quantity_dispensed += inv.stock_quantity
                    inv.stock_quantity = 0
                
                inv.save()
            item.save()

        prescription.status = Prescription.Status.DISPENSED
        prescription.save()

        return Response({"message": "Ordonnance délivrée avec succès et stocks mis à jour (FEFO)."}, status=status.HTTP_200_OK)