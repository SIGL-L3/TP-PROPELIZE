import json
from django.http import JsonResponse
from vehicule.models import Vehicule
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

    def post(self,request):
        data = json.loads(request.body)
        if request.method == "POST":
            required_fields = ["registration_number", "make", "model", "year", "rentalprice"]
            for field in required_fields:
                if field not in data:
                    return JsonResponse({"error": f"Le champ {field} est requis."}, status=400)

            vehicule = Vehicule.objects.create(
                registration_number=data["registration_number"],
                make=data["make"],
                model=data["model"],
                year=data["year"],
                rentalprice=data["rentalprice"]
            )
            print(data)
        print('test')
        print(vehicule)
        return Response({"Success Create vehicule"})

        def patch(self,request,pk):
            vehicule = get_object_or_404(Vehicule,pk=pk)

            serializer = VehiculeSerializer(vehicule,request.data,partial=True)

            if serializer.is_valid():
                serializer.save()
                return  Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)