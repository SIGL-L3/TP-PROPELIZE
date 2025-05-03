# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from vehicule.models import Vehicule

class SearchViewTests(TestCase):
    def setUp(self):
        # Arrange : Création de données de test
        Vehicule.objects.create(registration_number='ABC123', make='Honda' , model='Accord', rentalprice=100.0, year=2020)
        Vehicule.objects.create(registration_number='XYZ789', make='Toyota' , model='Camry', rentalprice=200.0, year=2025)

    def test_search_by_registration_success(self):
        # Arrange
        url = reverse('search_by_registration')
        registration_number = 'ABC123'

        # Act
        response = self.client.get(url, {'registration_number': registration_number})

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['registration_number'], registration_number)

    def test_search_by_registration_missing_param(self):
        # Arrange
        url = reverse('search_by_registration')

        # Act
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_search_by_price_success(self):
        # Arrange
        url = reverse('search_by_price')
        max_price = 150

        # Act
        response = self.client.get(url, {'max_price': max_price})

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertLessEqual(float(response.json()[0]['rentalprice']), max_price)


    def test_search_by_price_missing_param(self):
        # Arrange
        url = reverse('search_by_price')

        # Act
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_search_by_price_invalid_param(self):
        # Arrange
        url = reverse('search_by_price')
        invalid_price = 'invalid'

        # Act
        response = self.client.get(url, {'max_price': invalid_price})

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
