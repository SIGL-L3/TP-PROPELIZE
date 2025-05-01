from django.urls import path
from .views import  VehiculeView

urlpatterns = [
    path('delete/<int:pk>/', VehiculeView.as_view()),
]

