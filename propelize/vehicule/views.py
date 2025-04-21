from rest_framework.views import  APIView
from django.shortcuts import get_object_or_404
from .models import Vehicule
from rest_framework import  status

from .serializers import VehiculeSerializer
from rest_framework.response import  Response

class VehiculeView(APIView):
    def get(self,request,pk):
        vehicule = get_object_or_404(Vehicule,pk=pk)

        serializer = VehiculeSerializer(vehicule)
        return Response(serializer.data)

    def patch(self,request,pk):
        vehicule = get_object_or_404(Vehicule,pk=pk)

        serializer = VehiculeSerializer(vehicule,request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)