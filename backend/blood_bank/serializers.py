from rest_framework import serializers
from .models import BloodBank, BloodInventory


class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank
        fields = ['id', 'hospital_name', 'city', 'neighborhood', 'latitude', 'longitude']


class BloodInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodInventory
        fields = [
            'id', 'blood_bank', 'barcode_id', 'blood_group', 
            'component', 'status', 'collection_date', 'expiration_date'
        ]
        read_only_fields = ['id']

    def validate_blood_group(self, value):
        valid_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if value not in valid_groups:
            raise serializers.ValidationError("Groupe sanguin invalide.")
        return value