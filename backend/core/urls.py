from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('accounts.urls')), # Préfixe unifié API v1
    path('api/v1/prescriptions/', include('prescriptions.urls')),
]