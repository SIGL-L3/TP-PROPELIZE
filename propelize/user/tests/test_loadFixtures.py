from django.test import TestCase
from django.core.management import call_command
from decimal import Decimal
from ..models import User


class LoadAlluserFixtureTest(TestCase):
    EXPECTED_user_DATA = [
    {
        "model": "user.user",
        "pk": 1,
        "fields": {
            "name": "alice",
            "password": "Sunshine89!"
        }
    },
    {
        "model": "user.user",
        "pk": 2,
        "fields": {
            "name": "bob",
            "password": "ForestWalk22"
        }
    },
    {
        "model": "user.user",
        "pk": 3,
        "fields": {
            "name": "charlie",
            "password": "BlueOcean#1"
        }
    },
    {
        "model": "user.user",
        "pk": 4,
        "fields": {
            "name": "diana",
            "password": "CoffeeTime@7"
        }
    },
    {
        "model": "user.user",
        "pk": 5,
        "fields": {
            "name": "emilie",
            "password": "StrongPass9$"
        }
    },
    {
        "model": "user.user",
        "pk": 6,
        "fields": {
            "name": "frank",
            "password": "NightSky77!"
        }
    },
    {
        "model": "user.user",
        "pk": 7,
        "fields": {
            "name": "george",
            "password": "SecureMe21@"
        }
    },
    {
        "model": "user.user",
        "pk": 8,
        "fields": {
            "name": "hannah",
            "password": "TravelMore44"
        }
    },
    {
        "model": "user.user",
        "pk": 9,
        "fields": {
            "name": "ian",
            "password": "RiverSide55!"
        }
    },
    {
        "model": "user.user",
        "pk": 10,
        "fields": {
            "name": "julia",
            "password": "BookLover99"
        }
    },
    {
        "model": "user.user",
        "pk": 11,
        "fields": {
            "name": "kevin",
            "password": "Mountains8@"
        }
    },
    {
        "model": "user.user",
        "pk": 12,
        "fields": {
            "name": "laura",
            "password": "HappyDay33#"
        }
    },
    {
        "model": "user.user",
        "pk": 13,
        "fields": {
            "name": "michael",
            "password": "C0dingLife!"
        }
    },
    {
        "model": "user.user",
        "pk": 14,
        "fields": {
            "name": "nina",
            "password": "PianoKeys22"
        }
    },
    {
        "model": "user.user",
        "pk": 15,
        "fields": {
            "name": "olive",
            "password": "LongDrive66@"
        }
    },
    {
        "model": "user.user",
        "pk": 16,
        "fields": {
            "name": "paula",
            "password": "GoldenSun12"
        }
    },
    {
        "model": "user.user",
        "pk": 17,
        "fields": {
            "name": "quentin",
            "password": "RedWine34!"
        }
    },
    {
        "model": "user.user",
        "pk": 18,
        "fields": {
            "name": "rachel",
            "password": "Peace&Love9"
        }
    },
    {
        "model": "user.user",
        "pk": 19,
        "fields": {
            "name": "steve",
            "password": "BuildMore88"
        }
    },
    {
        "model": "user.user",
        "pk": 20,
        "fields": {
            "name": "tina",
            "password": "Cats&Books@"
        }
    }
]



    @classmethod
    def setUpTestData(cls):
        call_command('loadFixtures')

    def test_fixture_total_count(self):
        """Vérifie que le nombre total de user chargés correspond à celui attendu."""
        self.assertEqual(User.objects.count(), 20)
        self.assertEqual(len(self.EXPECTED_user_DATA), 20,
                         "Erreur dans la configuration des données de test attendues.")

    def test_all_user_details_are_correct(self):
        """Vérifie les détails de chaque user chargé à partir de la fixture."""

        for expected_data in self.EXPECTED_user_DATA:
            pk_to_check = expected_data["pk"]
            # Utiliser subTest pour isoler les échecs par user
            with self.subTest(user_pk=pk_to_check):
                try:
                    user_obj = User.objects.get(pk=pk_to_check)
                except User.DoesNotExist:
                    # Si l'objet n'existe pas, le test échoue immédiatement pour ce PK.
                    self.fail(f"Le user avec pk={pk_to_check} n'a pas été trouvé dans la base de données.")

                self.assertEqual(user_obj.name, expected_data["fields"]["name"])
                self.assertEqual(user_obj.password, expected_data["fields"]["password"])
            