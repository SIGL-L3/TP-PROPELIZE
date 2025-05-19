from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Vehicule


class VehiculeModelTest(TestCase):
    def setUp(self):
        self.vehiculle= Vehicule.objects.create(
            registration_number="AB123CD",
            make="Toyota",
            model="CHR",
            year=2020,
            rentalprice=15000.000
        )

    def test_vehicule_creations(self):
        self.assertEqual(self.vehiculle.make, "Toyota")
        self.assertEqual(self.vehiculle.registration_number, "AB123CD")
        self.assertEqual(self.vehiculle.model, "CHR")
        self.assertEqual(self.vehiculle.year, 2020)
        self.assertEqual(self.vehiculle.rentalprice, 15000.000)
        self.assertEqual(str(self.vehiculle),"Model:CHR,15000.0")

    def test_registration_number_unique(self):
        with self.assertRaises(Exception):
            Vehicule.objects.create(
                registration_number="AB123CD", # doublon
                make="Honda",
                model="Civic",
                year=2022,
                rentalprice=12000.000
            )

    def test_blank_fields(self):
        vehicule = Vehicule(
            registration_number="",
            make="",
            model="",
            year=2020,
            rentalprice=10000.000
        )
        
        with self.assertRaises(ValidationError):
            print(vehicule.full_clean())
    
    def test_negative_year(self):
        vehicule = Vehicule(
            registration_number="ZZ999ZZ",
            make="Peugeot",
            model="308",
            year=-2010,  # année invalide
            rentalprice=10000.0
        )

        with self.assertRaises(ValidationError):
            vehicule.full_clean()

    def test_invalid_rental_price(self):
        with self.assertRaises(Exception):
            vehicule = Vehicule(
                registration_number="WW123WW",
                make="Renault",
                model="Clio",
                year=2023,
                rentalprice="prix"  # mauvais type (string)
            )
            
    def test_str_method(self):
        vehicule = Vehicule.objects.create(
            registration_number="AA111AA",
            make="Toyota",
            model="Yaris",
            year=2021,
            rentalprice=12345.678
        )
        self.assertEqual(str(vehicule), "Model:Yaris,12345.678")