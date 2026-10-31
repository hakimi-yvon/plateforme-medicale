from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import BloodBank, BloodInventory
from .serializers import BloodBankSerializer, BloodInventorySerializer


class BloodBankListCreateView(generics.ListCreateAPIView):
    """Gestion des centres hospitaliers et banques de sang."""
    queryset = BloodBank.objects.all()
    serializer_class = BloodBankSerializer
    permission_classes = [permissions.IsAuthenticated]


class BloodInventoryListCreateView(generics.ListCreateAPIView):
    """Enregistrement et consultation des pochettes de sang en stock."""
    queryset = BloodInventory.objects.all()
    serializer_class = BloodInventorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = BloodInventory.objects.all()
        blood_group = self.request.query_params.get('blood_group')
        status_param = self.request.query_params.get('status', BloodInventory.Status.AVAILABLE)

        if blood_group:
            queryset = queryset.filter(blood_group=blood_group)
        if status_param:
            queryset = queryset.filter(status=status_param)
            
        # Priorisation FEFO (First Expired, First Out)
        return queryset.order_by('expiration_date')


class DispenseBloodBagView(APIView):
    """
    Délivrance d'urgence d'une pochette de sang selon la règle FEFO.
    """
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        blood_group = request.data.get('blood_group')
        component = request.data.get('component', BloodInventory.ComponentType.PACKED_RED_CELLS)

        if not blood_group:
            return Response({"error": "Le groupe sanguin est obligatoire."}, status=status.HTTP_400_BAD_REQUEST)

        # Sélection de la pochette disponible dont la date d'expiration est la plus proche (FEFO)
        blood_bag = BloodInventory.objects.filter(
            blood_group=blood_group,
            component=component,
            status=BloodInventory.Status.AVAILABLE
        ).order_by('expiration_date').first()

        if not blood_bag:
            return Response(
                {"error": f"Rupture de stock pour le groupe {blood_group}. Déclenchement d'alerte suggéré."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Mise à jour du statut transactionnel
        blood_bag.status = BloodInventory.Status.TRANSFUSED
        blood_bag.save()

        return Response({
            "message": "Pochette attribuée et sortie du stock avec succès (FEFO).",
            "pochette_id": blood_bag.barcode_id,
            "date_expiration": blood_bag.expiration_date
        }, status=status.HTTP_200_OK)