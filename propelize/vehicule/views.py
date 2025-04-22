from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vehicule

class DeleteVehiculeAPIView(APIView):
    
    def delete(self, request, pk):
        try:
            vehicule = Vehicule.objects.get(pk=pk)
            vehicule.delete()
            return Response({"message": "Vehicule supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
        
        except vehicule.DoesNotExist:
            return Response({"message": "Vehicule introuvable"}, status=status.HTTP_404_NOT_FOUND)