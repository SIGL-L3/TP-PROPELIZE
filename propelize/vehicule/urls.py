from django.urls import path
from vehicule.views import VehiculeView


urlpatterns = [
    path('create/',VehiculeView.as_view(), name='vehicule-list')
]
