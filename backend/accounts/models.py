import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        PATIENT = 'PATIENT', 'Patient'
        DOCTOR = 'DOCTOR', 'Médecin / Praticien'
        PHARMACIST = 'PHARMACIST', 'Pharmacien'
        BLOOD_BANK_MANAGER = 'BLOOD_BANK_MANAGER', 'Gestionnaire Banque de Sang'
        ADMIN = 'ADMIN', 'Administrateur'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=20, unique=True, db_index=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.PATIENT)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['phone_number', 'email']


class HealthPractitionerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='practitioner_profile')
    license_number = models.CharField(max_length=50, unique=True)
    specialty = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    public_key_pem = models.TextField(help_text="Clé publique RSA/ECDSA")


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    primary_account = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='dependents')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    blood_group = models.CharField(max_length=5, choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ], null=True, blank=True)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    is_eligible_donor = models.BooleanField(default=True)
    last_donation_date = models.DateField(null=True, blank=True)