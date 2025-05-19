from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vehicule

<<<<<<< HEAD
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
=======
from django.core.management import call_command
from vehicule.models import Vehicule

class LoadFixtureTest(TestCase):

    #cas de test1
    #test unitaire


#################Arrange#############################################
    V1={}
    V1=dict()
    V1={
        "registration_number": "ABC123",
            "make": "Toyota",
            "model": "Corolla",
            "year": 2020,
            "rentalprice": 150.000
    }

    V2={}
    V2=dict()

    V2={
        "registration_number": "XYZ456",
            "make": "Honda",
            "model": "Civic",
            "year": 2019,
            "rentalprice": 120.000
    }



    V3={}
    V3=dict()

    V3={
            "registration_number": "LMN789",
            "make": "Ford",
            "model": "Focus",
            "year": 2021,
            "rentalprice": 180.000
        }




    V4={}
    V4=dict()
    V4={"registration_number": "PQR321",
            "make": "BMW",
            "model": "320i",
            "year": 2022,
            "rentalprice": 250.000
        }




########Act#########################################################
    @classmethod
    def setUpTestData(cls):
        call_command('load_fixtures')
        cls.obj1= Vehicule.objects.get(pk=1)
        cls.obj2=Vehicule.objects.get(pk=2)
        cls.obj3=Vehicule.objects.get(pk=3)
        cls.obj4=Vehicule.objects.get(pk=4)


###############Assert##############################################
    def test_load_objec1(self):
        self.assertEqual(self.obj1.registration_number, "ABC123")
        self.assertEqual(self.obj1.make, "Toyota")
        self.assertEqual(self.obj1.model, "Corolla")
        self.assertEqual(self.obj1.year, 2020)
        self.assertEqual(self.obj1.rentalprice, 150.000)



    def test_load_objet2(self):
        self.assertEqual(self.obj2.registration_number,"XYZ456")
        self.assertEqual(self.obj2.make,"Honda")
        self.assertEqual(self.obj2.model,"Civic")
        self.assertEqual(self.obj2.year, 2019)
        self.assertEqual(self.obj2.rentalprice, 120.000)
      
 


    def test_load_objet3(self):
        self.assertEqual(self.obj3.registration_number,"LMN789")
        self.assertEqual(self.obj3.make,"Ford")
        self.assertEqual(self.obj3.model,"Focus")
        self.assertEqual(self.obj3.year, 2021)
        self.assertEqual(self.obj3.rentalprice, 180.000)


    def test_load_objet4(self):
        self.assertEqual(self.obj4.registration_number,"PQR321")
        self.assertEqual(self.obj4.make,"BMW")
        self.assertEqual(self.obj4.model,"320i")
        self.assertEqual(self.obj4.year, 2022)
        self.assertEqual(self.obj4.rentalprice, 250.000)
      


    def test_fixture_count(self):
        self.assertEqual(Vehicule.objects.count(),4)



########Test by yvanna
>>>>>>> 3b13920b0d0d977cae2249ea34d4dccde3010c53
