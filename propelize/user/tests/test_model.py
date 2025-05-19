from django.db import IntegrityError
from django.test import TestCase
from ..models import User
from ..serializers import UserSerializer

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            name="Olive",
            password="Olive@43215"
        )

        serializer = UserSerializer(data={"name": "Olive2","password": "Olive@43215"})
        if serializer.is_valid():
            self.user_serializer=serializer.save()


    def test_user_creation(self):
        self.assertEqual(self.user.name,"Olive")
        self.assertTrue(self.user_serializer.check_password("Olive@43215"))

    def test_user_creation_with_serializer(self):
        self.assertEqual(self.user_serializer.name, "Olive2")
        self.assertTrue(self.user_serializer.check_password("Olive@43215"))

    def test_user_creation_with_blank_name(self):
        with self.assertRaises(ValueError):
            user = User.objects.create_user(name="", password="Tracy@43215")

    def test_user_creation_without_password(self):
        with self.assertRaises(ValueError):
            user = User.objects.create_user(name="Tracy", password="")

    def test_user_creation_with_same_names(self):
        with self.assertRaises(IntegrityError):
            self.user = User.objects.create_user(
                name="Olive",
                password="Olive@43215"
            )