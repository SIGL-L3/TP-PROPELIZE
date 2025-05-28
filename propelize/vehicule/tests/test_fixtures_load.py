from django.test import TestCase
from django.core.management import call_command
from decimal import Decimal
from ..models import Vehicule


class LoadAllVehiclesFixtureTest(TestCase):
    EXPECTED_VEHICLES_DATA = [
        {
            "pk": 1, "registration_number": "AB-123-CD", "make": "Toyota", "model": "Corolla",
            "year": 2020, "rentalprice": Decimal("150.00")
        },
        {
            "pk": 2, "registration_number": "EF-456-GH", "make": "Honda", "model": "Civic",
            "year": 2019, "rentalprice": Decimal("120.00")
        },
        {
            "pk": 3, "registration_number": "IJ-789-KL", "make": "Ford", "model": "Focus",
            "year": 2021, "rentalprice": Decimal("180.00")
        },
        {
            "pk": 4, "registration_number": "MN-321-OP", "make": "BMW", "model": "320i",
            "year": 2022, "rentalprice": Decimal("250.00")
        },
        {
            "pk": 5, "registration_number": "QR-654-ST", "make": "Volkswagen", "model": "Golf",
            "year": 2021, "rentalprice": Decimal("165.00")
        },
        {
            "pk": 6, "registration_number": "UV-987-WX", "make": "Audi", "model": "A3",
            "year": 2022, "rentalprice": Decimal("220.00")
        },
        {
            "pk": 7, "registration_number": "YZ-111-AB", "make": "Mercedes-Benz", "model": "A-Class",
            "year": 2021, "rentalprice": Decimal("230.00")
        },
        {
            "pk": 8, "registration_number": "BC-222-DE", "make": "Renault", "model": "Clio",
            "year": 2023, "rentalprice": Decimal("95.00")
        },
        {
            "pk": 9, "registration_number": "FG-333-HI", "make": "Peugeot", "model": "208",
            "year": 2022, "rentalprice": Decimal("110.00")
        },
        {
            "pk": 10, "registration_number": "JK-444-LM", "make": "Hyundai", "model": "i30",
            "year": 2020, "rentalprice": Decimal("135.00")
        },
        {
            "pk": 11, "registration_number": "NO-555-PQ", "make": "Kia", "model": "Ceed",
            "year": 2021, "rentalprice": Decimal("140.00")
        },
        {
            "pk": 12, "registration_number": "RS-666-TU", "make": "Ford", "model": "Mustang",
            "year": 2019, "rentalprice": Decimal("280.00")
        },
        {
            "pk": 13, "registration_number": "VW-777-XY", "make": "Toyota", "model": "RAV4",
            "year": 2022, "rentalprice": Decimal("190.00")
        },
        {
            "pk": 14, "registration_number": "ZA-888-BC", "make": "Honda", "model": "CR-V",
            "year": 2020, "rentalprice": Decimal("185.00")
        },
        {
            "pk": 15, "registration_number": "DE-999-FG", "make": "BMW", "model": "X5",
            "year": 2021, "rentalprice": Decimal("350.00")
        },
        {
            "pk": 16, "registration_number": "HI-101-JK", "make": "Audi", "model": "Q5",
            "year": 2020, "rentalprice": Decimal("320.00")
        },
        {
            "pk": 17, "registration_number": "LM-202-NO", "make": "Peugeot", "model": "3008",
            "year": 2023, "rentalprice": Decimal("210.00")
        },
        {
            "pk": 18, "registration_number": "PQ-303-RS", "make": "Volkswagen", "model": "Passat",
            "year": 2019, "rentalprice": Decimal("175.00")
        },
        {
            "pk": 19, "registration_number": "TU-404-VW", "make": "Tesla", "model": "Model 3",
            "year": 2022, "rentalprice": Decimal("300.00")
        },
        {
            "pk": 20, "registration_number": "XY-505-ZA", "make": "Renault", "model": "Captur",
            "year": 2021, "rentalprice": Decimal("155.00")
        }
    ]

    @classmethod
    def setUpTestData(cls):
        call_command('load_fixtures')

    def test_fixture_total_count(self):
        """Vérifie que le nombre total de véhicules chargés correspond à celui attendu."""
        self.assertEqual(Vehicule.objects.count(), 20)
        self.assertEqual(len(self.EXPECTED_VEHICLES_DATA), 20,
                         "Erreur dans la configuration des données de test attendues.")

    def test_all_vehicles_details_are_correct(self):
        """Vérifie les détails de chaque véhicule chargé à partir de la fixture."""

        for expected_data in self.EXPECTED_VEHICLES_DATA:
            pk_to_check = expected_data["pk"]
            # Utiliser subTest pour isoler les échecs par véhicule
            with self.subTest(vehicle_pk=pk_to_check):
                try:
                    vehicle_obj = Vehicule.objects.get(pk=pk_to_check)
                except Vehicule.DoesNotExist:
                    # Si l'objet n'existe pas, le test échoue immédiatement pour ce PK.
                    self.fail(f"Le véhicule avec pk={pk_to_check} n'a pas été trouvé dans la base de données.")

                self.assertEqual(vehicle_obj.registration_number, expected_data["registration_number"])
                self.assertEqual(vehicle_obj.make, expected_data["make"])
                self.assertEqual(vehicle_obj.model, expected_data["model"])
                self.assertEqual(vehicle_obj.year, expected_data["year"])
                self.assertEqual(vehicle_obj.rentalprice, expected_data["rentalprice"])