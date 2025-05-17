from rest_framework.views import  APIView
from django.shortcuts import get_object_or_404
from .models import Vehicule
from rest_framework import  status

from .serializers import VehiculeSerializer
from rest_framework.response import  Response

from django.http import JsonResponse
from django.views import View



class VehiculeView(APIView):
    def get(self,request,pk):
        vehicule = get_object_or_404(Vehicule,pk=pk)

        serializer = VehiculeSerializer(vehicule)
        return Response(serializer.data)


    def post(self, request):
        serializer = VehiculeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        vehicule = get_object_or_404(Vehicule,pk=pk)

        serializer = VehiculeSerializer(vehicule,request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vehicule = get_object_or_404(Vehicule,pk=pk)
        vehicule.delete()
        return Response(status=status.HTTP_200_OK)
# Recherche par immatriculation (exact match)
class SearchByRegistrationView(View):
    def get(self, request):
        registration_number = request.GET.get('registration_number')
        if not registration_number:
            return JsonResponse({'error': 'registration_number parameter is required'}, status=400)

        vehicules = Vehicule.objects.filter(registration_number=registration_number)
        data = list(vehicules.values())
        return JsonResponse(data, safe=False)

# Recherche par prix maximum
class SearchByPriceView(View):
    def get(self, request):
        max_price = request.GET.get('max_price')
        if not max_price:
            return JsonResponse({'error': 'max_price parameter is required'}, status=400)

        try:
            max_price = float(max_price)
        except ValueError:
            return JsonResponse({'error': 'max_price must be a number'}, status=400)

        vehicules = Vehicule.objects.filter(rentalprice__lte=max_price)
        data = list(vehicules.values())
        return JsonResponse(data, safe=False)
