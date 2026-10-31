from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, PatientProfile, HealthPractitionerProfile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone_number', 'role', 'is_verified', 'is_staff')
    list_filter = ('role', 'is_verified', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informations Métier RBAC', {'fields': ('phone_number', 'role', 'is_verified')}),
    )

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'city', 'is_eligible_donor')
    search_fields = ('user__username', 'user__phone_number', 'city')

@admin.register(HealthPractitionerProfile)
class HealthPractitionerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number', 'specialty', 'city')
    search_fields = ('license_number', 'user__username')