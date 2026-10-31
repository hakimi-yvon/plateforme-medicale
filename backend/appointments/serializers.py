from rest_framework import serializers
from .models import Appointment, Payment
from accounts.models import HealthPractitionerProfile


class AppointmentCreateSerializer(serializers.ModelSerializer):
    doctor_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'doctor_id', 'appointment_date', 'mode', 'status']
        read_only_fields = ['id', 'status']


class PaymentInitiateSerializer(serializers.ModelSerializer):
    appointment_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'appointment_id', 'amount', 'payment_channel', 'transaction_reference', 'status']
        read_only_fields = ['id', 'transaction_reference', 'status']