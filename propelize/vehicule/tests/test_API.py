from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Vehicule
from django.test import TestCase
from django.core.management import call_command



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


class VehiculeIntegrationTest(APITestCase):

    def test_crud_workflow(self):
        #  CREATE
        create_url = reverse('vehicule-create') 
        data_create = {
            "registration_number": "ZZ999ZZ",
            "make": "Peugeot",
            "model": "308",
            "year": 2023,
            "rentalprice": 100.0
        }
        response = self.client.post(create_url, data_create, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        vehicule_id = response.data['id']  # récupère l'id créé

        #  READ
        detail_url = reverse('vehicule-detail', kwargs={'pk': vehicule_id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['registration_number'], data_create['registration_number'])

        #  UPDATE
        update_url = reverse('vehicule-update', kwargs={'pk': vehicule_id})
        data_update = {
            "registration_number": "ZZ999ZZ",
            "make": "Peugeot",
            "model": "308 GT",
            "year": 2023,
            "rentalprice": 120.0
        }
        response = self.client.patch(update_url, data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['model'], "308 GT")
        self.assertEqual(float(response.data['rentalprice']), 120.0)


        #  DELETE (si tu as un endpoint de suppression)
        delete_url = reverse('vehicule-delete', kwargs={'pk': vehicule_id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        #  Vérifier que le véhicule est bien supprimé
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)