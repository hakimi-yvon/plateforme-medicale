from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    RegisterPatientView,
    RegisterPractitionerView,
    UserProfileView
)

urlpatterns = [
    # Inscriptions
    path('register/patient/', RegisterPatientView.as_view(), name='register-patient'),
    path('register/practitioner/', RegisterPractitionerView.as_view(), name='register-practitioner'),

    # Tokens JWT
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Profil Utilisateur courant
    path('me/', UserProfileView.as_view(), name='user-me'),
]