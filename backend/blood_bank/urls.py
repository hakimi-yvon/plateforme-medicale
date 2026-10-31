from django.urls import path
from .views import BloodBankListCreateView, BloodInventoryListCreateView, DispenseBloodBagView

urlpatterns = [
    path('banks/', BloodBankListCreateView.as_view(), name='blood-bank-list'),
    path('inventory/', BloodInventoryListCreateView.as_view(), name='blood-inventory-list'),
    path('inventory/dispense/', DispenseBloodBagView.as_view(), name='blood-inventory-dispense'),
]