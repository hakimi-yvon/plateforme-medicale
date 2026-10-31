from django.urls import path
from .views import BookAppointmentView, InitiatePaymentView, MobileMoneyWebhookView

urlpatterns = [
    path('book/', BookAppointmentView.as_view(), name='book-appointment'),
    path('payment/initiate/', InitiatePaymentView.as_view(), name='initiate-payment'),
    path('payment/webhook/mobile-money/', MobileMoneyWebhookView.as_view(), name='mobile-money-webhook'),
]