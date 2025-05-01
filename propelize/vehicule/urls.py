from django.urls import  path
from .views import  VehiculeView

urlpatterns = [
    path('get/<int:pk>/',VehiculeView.as_view()),
    path('update/<int:pk>/',VehiculeView.as_view()),
    path('create/',VehiculeView.as_view()),
    path('delete/<int:pk>/', VehiculeView.as_view()),
]