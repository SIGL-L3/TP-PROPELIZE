from django.urls import path
from .views import VehiculeView

urlpatterns = [
    path('api/vehicule/', VehiculeView.as_view(), name='vehicule-list'),
    path('api/vehicule/<int:pk>/', VehiculeView.as_view(), name='vehicule-detail'),
]