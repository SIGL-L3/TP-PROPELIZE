# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vehicule
import os
import json
from django.conf import settings

class VehiculeCreateTests(APITestCase):
    """Tests pour l'endpoint de création de véhicule"""
    
    def setUp(self):
        """Configuration pour chaque test"""
        self.valid_payload = {
            'registration_number': 'DEF789', 
            'make': 'Toyota',
            'model': 'Camry',
            'year': 2022,
            'rentalprice': '200.000'
        }
        
        self.invalid_payload = {
            'registration_number': '',  # Numéro d'immatriculation vide (champ obligatoire)
            'make': 'Toyota',
            'model': 'Corolla',
            'year': 2022,
            'rentalprice': '150.000'
        }
    
    def test_create_valid_vehicule(self):
        """Test de création d'un nouveau véhicule avec des données valides"""
        url = reverse('vehicule-create')
        response = self.client.post(url, self.valid_payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vehicule.objects.count(), 1)
        vehicule = Vehicule.objects.get()
        self.assertEqual(vehicule.registration_number, 'DEF789')
        self.assertEqual(vehicule.make, 'Toyota')
        self.assertEqual(vehicule.model, 'Camry')
    
    def test_create_invalid_vehicule(self):
        """Test de création d'un nouveau véhicule avec des données invalides"""
        url = reverse('vehicule-create')
        response = self.client.post(url, self.invalid_payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Vehicule.objects.count(), 0)
    
    def test_duplicate_registration_number(self):
        """Test qu'on ne peut pas créer des véhicules avec des numéros d'immatriculation dupliqués"""
        # Crée d'abord un véhicule
        url = reverse('vehicule-create')
        self.client.post(url, self.valid_payload, format='json')
        
        # Essaie d'en créer un autre avec le même numéro d'immatriculation
        duplicate_payload = {
            'registration_number': 'DEF789',  # Même numéro d'immatriculation
            'make': 'Honda',
            'model': 'Accord',
            'year': 2021,
            'rentalprice': '180.000'
        }
        
        response = self.client.post(url, duplicate_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Vehicule.objects.count(), 1)  # Toujours un seul véhicule

class FixtureLoadTests(APITestCase):
    """Tests pour le chargement des fixtures"""
    
    def setUp(self):
        # Crée un fichier fixture temporaire pour les tests
        self.fixture_data = [
            {
                "model": "propelize.vehicule",
                "pk": 1,
                "fields": {
                    "registration_number": "ABC123",
                    "make": "Toyota",
                    "model": "Corolla",
                    "year": 2020,
                    "rentalprice": "150.000"
                }
            },
            {
                "model": "propelize.vehicule",
                "pk": 2,
                "fields": {
                    "registration_number": "XYZ456",
                    "make": "Honda",
                    "model": "Civic",
                    "year": 2019,
                    "rentalprice": "120.000"
                }
            }
        ]
        
        # Assurez-vous que le répertoire fixtures existe
        os.makedirs(os.path.join(settings.BASE_DIR, 'fixtures'), exist_ok=True)
        
        # Écrit les données dans le fichier fixture
        with open(os.path.join(settings.BASE_DIR, 'fixtures', 'test_vehicles.json'), 'w') as f:
            json.dump(self.fixture_data, f)
    
    def test_load_fixtures_endpoint(self):
        """Test de l'endpoint de chargement des fixtures"""
        url = reverse('load-fixtures')
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Vérifie que les véhicules ont été créés
        self.assertEqual(Vehicule.objects.count(), 2)
        
        # Vérifie les données spécifiques
        vehicule1 = Vehicule.objects.get(registration_number="ABC123")
        self.assertEqual(vehicule1.make, "Toyota")
        self.assertEqual(vehicule1.model, "Corolla")
        
        vehicule2 = Vehicule.objects.get(registration_number="XYZ456")
        self.assertEqual(vehicule2.make, "Honda")
        self.assertEqual(vehicule2.model, "Civic")
    
    def tearDown(self):
        """Nettoie après chaque test"""
        # Supprime le fichier fixture temporaire
        try:
            os.remove(os.path.join(settings.BASE_DIR, 'fixtures', 'test_vehicles.json'))
        except:
            pass