from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Vehicule

class VehiculeAPITest(APITestCase):
    def setUp(self):
        self.vehicule = Vehicule.objects.create(
            registration_number="123XYZ",
            make="Toyota",
            model="CHR",
            year=2022,
            rentalprice=100.000
        )
    
    def test_get_single_vehicule(self):
        url = reverse('vehicule-detail', kwargs={'pk': self.vehicule.pk}) 
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['model'], "CHR")
