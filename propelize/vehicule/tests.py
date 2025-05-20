from django.test import TestCase

from django.core.management import call_command
from .models import Vehicule

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