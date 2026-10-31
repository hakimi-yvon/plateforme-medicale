from rest_framework import serializers
from .models import Prescription, PrescriptionItem, Pharmacy, PharmacyInventory
from accounts.models import PatientProfile


class PrescriptionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionItem
        fields = ['id', 'medication_name', 'dosage', 'posology', 'duration_days', 'quantity_prescribed', 'quantity_dispensed']


class PrescriptionCreateSerializer(serializers.ModelSerializer):
    items = PrescriptionItemSerializer(many=True)
    patient_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Prescription
        fields = ['id', 'patient_id', 'items', 'sha256_hash', 'digital_signature', 'qr_code_token', 'created_at']
        read_only_fields = ['sha256_hash', 'digital_signature', 'qr_code_token', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        patient_id = validated_data.pop('patient_id')
        doctor = self.context['request'].user.practitioner_profile
        patient = PatientProfile.objects.get(id=patient_id)

        # 1. Calcul du hachage SHA-256
        sha256_hash = generate_prescription_hash(items_data)

        # 2. Simulation / Application du tampon cryptographique (Clé Privée)
        # En production, la clé privée est transmise de manière sécurisée par l'application client
        qr_token = str(uuid.uuid4())

        prescription = Prescription.objects.create(
            doctor=doctor,
            patient=patient,
            sha256_hash=sha256_hash,
            digital_signature="SIGNATURE_CRYPTOGRAPHIQUE_RSA_HEX",
            qr_code_token=qr_token
        )

        for item in items_data:
            PrescriptionItem.objects.create(prescription=prescription, **item)

        return prescription


class PharmacyInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyInventory
        fields = ['id', 'medication_name', 'batch_number', 'expiration_date', 'stock_quantity', 'unit_price', 'reorder_threshold']