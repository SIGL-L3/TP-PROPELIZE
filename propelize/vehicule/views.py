from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import VehiculeSerializer
from .models import Vehicule  

class VehiculeViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les opérations CRUD sur les véhicules
    """
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer