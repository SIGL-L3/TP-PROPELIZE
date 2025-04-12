from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.management import call_command
from .models import Vehicule
from vehicule.serializers import VehiculeSerializer
import os
import json

class VehiculeCreateAPIView(APIView):
    """
    API endpoint pour créer un véhicule
    """
    def post(self, request, format=None):
        serializer = VehiculeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def load_fixtures(request):
    """
    Charge les données depuis le fichier fixture
    """
    fixture_path = os.path.join('fixtures', 'intitial_data.json')
    
    try:
        with open(fixture_path, 'r') as file:
            fixtures = json.load(file)
            
        for fixture in fixtures:
            if fixture['model'] == 'propelize.vehicule':
                # Vérifie si le véhicule existe déjà
                exists = Vehicule.objects.filter(registration_number=fixture['fields']['registration_number']).exists()
                if not exists:
                    Vehicule.objects.create(
                        id=fixture['pk'],
                        registration_number=fixture['fields']['registration_number'],
                        make=fixture['fields']['make'],
                        model=fixture['fields']['model'],
                        year=fixture['fields']['year'],
                        rentalprice=fixture['fields']['rentalprice']
                    )
        
        return Response({"message": "Fixtures chargées avec succès"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Méthode pour utiliser à l'initialisation de l'application
def load_initial_data():
    """
    Fonction à appeler dans apps.py ready() pour charger les données au démarrage
    """
    fixture_path = os.path.join('fixtures', 'intitial_data.json')
    
    try:
        # Vérifie si des données existent déjà
        if Vehicule.objects.count() == 0:
            try:
                # Essaie d'abord la méthode Django
                call_command('loaddata', fixture_path)
            except:
                # Chargement manuel en cas d'échec
                with open(fixture_path, 'r') as file:
                    fixtures = json.load(file)
                
                for fixture in fixtures:
                    if fixture['model'] == 'propelize.vehicule':
                        Vehicule.objects.create(
                            id=fixture['pk'],
                            registration_number=fixture['fields']['registration_number'],
                            make=fixture['fields']['make'],
                            model=fixture['fields']['model'],
                            year=fixture['fields']['year'],
                            rentalprice=fixture['fields']['rentalprice']
                        )
    except Exception as e:
        print(f"Erreur lors du chargement des fixtures: {e}")