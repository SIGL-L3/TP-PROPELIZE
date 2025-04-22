from django.urls import path
from .views import  DeleteVehiculeAPIView

urlpatterns = [
    path('vehicules/<int:pk>/', DeleteVehiculeAPIView.as_view(), name='vehicule-detail'),
]

