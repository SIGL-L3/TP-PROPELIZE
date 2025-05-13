from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vehicule

class VehiculeDeleteTestCase(APITestCase):

    def setUp(self):
        self.vehicule = Vehicule.objects.create(
            registration_number="ABC123XYZ",
            make="Toyota",
            model="Corolla",
            year=2020,
            rentalprice=150.000
        )
        self.delete_url = reverse('vehicule-detail', kwargs={'pk': self.vehicule.pk})

    def test_delete_vehicule_success(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Vehicule.objects.filter(pk=self.vehicule.pk).exists())

    def test_delete_vehicule_not_found(self):
        invalid_url = reverse('vehicule-detail', kwargs={'pk': 9999})
        response = self.client.delete(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_vehicule_invalid_pk_type(self):
        # Remplace '/api/vehicule/abc/' par ton endpoint réel
        response = self.client.delete('/api/vehicule/abc/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
