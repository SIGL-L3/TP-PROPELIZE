from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vehicule
from django.shortcuts import get_object_or_404

class VehiculeView(APIView):
    
    def delete(self, request, pk):
        vehicule = get_object_or_404(Vehicule,pk=pk)
        vehicule.delete()
        return Response(status=status.HTTP_200_OK)