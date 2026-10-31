from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, PatientProfile, HealthPractitionerProfile


# --- Customisation des claims dans le Token JWT ---
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Inclusion des rôles et informations clés dans le jeton JWT
        token['username'] = user.username
        token['phone_number'] = user.phone_number
        token['role'] = user.role
        token['is_verified'] = user.is_verified
        return token


# --- Sérialiseur d'Inscription Patient ---
class PatientRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    city = serializers.CharField(write_only=True)
    neighborhood = serializers.CharField(write_only=True)
    gender = serializers.CharField(write_only=True)
    date_of_birth = serializers.DateField(write_only=True, required=False)
    blood_group = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'phone_number', 'email', 'password',
            'city', 'neighborhood', 'gender', 'date_of_birth', 'blood_group'
        ]

    def create(self, validated_data):
        # Extraire les champs spécifiques au PatientProfile
        city = validated_data.pop('city')
        neighborhood = validated_data.pop('neighborhood')
        gender = validated_data.pop('gender')
        date_of_birth = validated_data.pop('date_of_birth', None)
        blood_group = validated_data.pop('blood_group', None)

        # Création de l'utilisateur avec le rôle PATIENT
        user = User.objects.create_user(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=User.Role.PATIENT,
            is_verified=True # Validé automatiquement par OTP en prod
        )

        # Création automatique du profil patient lié
        PatientProfile.objects.create(
            user=user,
            city=city,
            neighborhood=neighborhood,
            gender=gender,
            date_of_birth=date_of_birth,
            blood_group=blood_group
        )
        return user


# --- Sérialiseur d'Inscription Praticien / Pharmacien ---
class PractitionerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    license_number = serializers.CharField(write_only=True)
    specialty = serializers.CharField(write_only=True, required=False)
    city = serializers.CharField(write_only=True)
    neighborhood = serializers.CharField(write_only=True)
    consultation_fee = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True)
    public_key_pem = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'phone_number', 'email', 'password', 'role',
            'license_number', 'specialty', 'city', 'neighborhood', 'consultation_fee', 'public_key_pem'
        ]

    def create(self, validated_data):
        license_number = validated_data.pop('license_number')
        specialty = validated_data.pop('specialty', None)
        city = validated_data.pop('city')
        neighborhood = validated_data.pop('neighborhood')
        consultation_fee = validated_data.pop('consultation_fee', 0.00)
        public_key_pem = validated_data.pop('public_key_pem')

        role = validated_data.get('role', User.Role.DOCTOR)

        user = User.objects.create_user(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=role,
            is_verified=False # Soumis à vérification administrative
        )

        HealthPractitionerProfile.objects.create(
            user=user,
            license_number=license_number,
            specialty=specialty,
            city=city,
            neighborhood=neighborhood,
            consultation_fee=consultation_fee,
            public_key_pem=public_key_pem
        )
        return user


# --- Sérialiseur d'Affichage Utilisateur ---
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'email', 'role', 'is_verified', 'created_at']