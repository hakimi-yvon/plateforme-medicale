from django.urls import path
from .views import CreatePrescriptionView, VerifyAndDispensePrescriptionView

urlpatterns = [
    path('issue/', CreatePrescriptionView.as_view(), name='issue-prescription'),
    path('dispense/<str:qr_code_token>/', VerifyAndDispensePrescriptionView.as_view(), name='dispense-prescription'),
]