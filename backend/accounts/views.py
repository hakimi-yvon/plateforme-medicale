from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import (
    CustomTokenObtainPairSerializer,
    PatientRegistrationSerializer,
    PractitionerRegistrationSerializer,
    UserDetailSerializer
)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterPatientView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PatientRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class RegisterPractitionerView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PractitionerRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)