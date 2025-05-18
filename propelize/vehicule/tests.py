from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vehicule
import unittest
import json


class VehiculeTests(APITestCase):
    """Tests pour les opérations CRUD sur les véhicules"""

    def setUp(self):
        """Configuration pour chaque test"""
        self.valid_payload = {
            'registration_number': 'DEF789',
            'make': 'Toyota',
            'model': 'Camry',
            'year': 2022,
            'rentalprice': 200000  # note : en entier, pas string
        }

        self.invalid_payload = {
            'make': 'Toyota',
            'model': 'Corolla',
            'year': 2022,
            'rentalprice': 150000
            # registration_number manquant
        }

        print("\nPréparation du test...")

    def test_create_valid_vehicule(self):
        """Test de création d'un nouveau véhicule avec des données valides"""
        print("\nExécution du test de création avec données valides...")
        url = reverse('vehicule-list')  # Assure-toi que ce nom est correct dans urls.py

        response = self.client.post(url, data=json.dumps(self.valid_payload), content_type='application/json')

        try:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
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
        url = reverse('vehicule-list')

        response = self.client.post(url, data=json.dumps(self.invalid_payload), content_type='application/json')

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
        url = reverse('vehicule-list')

        first_response = self.client.post(url, data=json.dumps(self.valid_payload), content_type='application/json')

        if first_response.status_code != status.HTTP_200_OK:
            print(f"❌ Test échoué : Impossible de créer le premier véhicule. Statut: {first_response.status_code}")
            self.fail("La création du premier véhicule a échoué")

        duplicate_payload = {
            'registration_number': 'DEF789',  # même immatriculation
            'make': 'Honda',
            'model': 'Accord',
            'year': 2021,
            'rentalprice': 180000
        }

        response = self.client.post(url, data=json.dumps(duplicate_payload), content_type='application/json')

        try:
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(Vehicule.objects.count(), 1)
            print("✅ Test réussi : Détection correcte de la duplication du numéro d'immatriculation")
        except AssertionError as e:
            print(f"❌ Test échoué : {str(e)}")
            raise

    @classmethod
    def tearDownClass(cls):
        print("\nTests terminés. Nettoyage...")
        super().tearDownClass()
        print("Résumé des tests : voir résultats au-dessus.")


if __name__ == '__main__':
    unittest.main()
