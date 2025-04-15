# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vehicule
from django.conf import settings
import unittest

class VehiculeTests(APITestCase):
    """Tests pour les opérations CRUD sur les véhicules"""
    
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
        print("\nPréparation du test...")
    
    def test_create_valid_vehicule(self):
        """Test de création d'un nouveau véhicule avec des données valides"""
        print("\nExécution du test de création avec données valides...")
        url = reverse('vehicule-list')  # Utilise le nom standard du ViewSet
        response = self.client.post(url, self.valid_payload, format='json')
        
        try:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Vehicule.objects.count(), 1)
            vehicule = Vehicule.objects.get()
            self.assertEqual(vehicule.registration_number, 'DEF789')
            self.assertEqual(vehicule.make, 'Toyota')
            self.assertEqual(vehicule.model, 'Camry')
            print("✅ Test réussi : Création d'un véhicule valide")
        except AssertionError as e:
            print(f"❌ Test échoué : {str(e)}")
            raise
    
    def test_create_invalid_vehicule(self):
        """Test de création d'un nouveau véhicule avec des données invalides"""
        print("\nExécution du test de création avec données invalides...")
        url = reverse('vehicule-list')  # Utilise le nom standard du ViewSet
        response = self.client.post(url, self.invalid_payload, format='json')
        
        try:
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(Vehicule.objects.count(), 0)
            print("✅ Test réussi : Rejet correct des données invalides")
        except AssertionError as e:
            print(f"❌ Test échoué : {str(e)}")
            raise
    
    def test_duplicate_registration_number(self):
        """Test qu'on ne peut pas créer des véhicules avec des numéros d'immatriculation dupliqués"""
        print("\nExécution du test de duplication de numéro d'immatriculation...")
        # Crée d'abord un véhicule
        url = reverse('vehicule-list')  # Utilise le nom standard du ViewSet
        first_response = self.client.post(url, self.valid_payload, format='json')
        
        if first_response.status_code != status.HTTP_201_CREATED:
            print(f"❌ Test échoué : Impossible de créer le premier véhicule. Statut: {first_response.status_code}")
            self.fail("La création du premier véhicule a échoué")
            
        # Essaie d'en créer un autre avec le même numéro d'immatriculation
        duplicate_payload = {
            'registration_number': 'DEF789',  # Même numéro d'immatriculation
            'make': 'Honda',
            'model': 'Accord',
            'year': 2021,
            'rentalprice': '180.000'
        }
        response = self.client.post(url, duplicate_payload, format='json')
        
        try:
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(Vehicule.objects.count(), 1)  # Toujours un seul véhicule
            print("✅ Test réussi : Détection correcte de la duplication du numéro d'immatriculation")
        except AssertionError as e:
            print(f"❌ Test échoué : {str(e)}")
            raise
    
    @classmethod
    def tearDownClass(cls):
        """Nettoyage après tous les tests"""
        print("\nTests terminés. Nettoyage...")
        super().tearDownClass()
        print("Résumé des tests:")
        # Notez que ce résumé n'est pas dynamique car Python ne fournit pas facilement
        # cette information dans tearDownClass


if __name__ == '__main__':
    unittest.main()