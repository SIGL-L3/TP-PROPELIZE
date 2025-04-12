from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.management import call_command
from .models import Vehicule
from .serializers import VehiculeSerializer
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
    fixture_path = os.path.join('propelize', 'fixtures', 'intitial_data.json')
    
    try:
        # Méthode 1: Utiliser Django loaddata
        call_command('loaddata', fixture_path)
        return Response({"message": "Fixtures chargées avec succès"}, status=status.HTTP_200_OK)
    except Exception as e:
        # Méthode 2: Charger manuellement si la méthode 1 échoue
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
            
            return Response({"message": "Fixtures chargées manuellement avec succès"}, status=status.HTTP_200_OK)
        except Exception as inner_e:
            return Response({"error": str(inner_e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def load_initial_data():
    """
    Charger les données au démarrage
    """
    fixture_path = os.path.join('fixtures', 'intitial_data.json')
    
    try:
        # Vérifie si des données existent déjà
        if Vehicule.objects.count() == 0:
            try:
                # Essaie d'abord la méthode Django
                call_command('loaddata', fixture_path)
            except Exception:
                # Chargement manuel en cas d'échec
                try:
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
                except Exception as file_error:
                    print(f"Erreur lors du chargement manuel des fixtures: {file_error}")
    except Exception as e:
        print(f"Erreur lors du chargement des fixtures: {e}")