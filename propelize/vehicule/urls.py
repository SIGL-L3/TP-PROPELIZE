from django.urls import  path
from .views import  VehiculeView
from .views import SearchByRegistrationView, SearchByPriceView

urlpatterns = [
    path('get/<int:pk>/',VehiculeView.as_view(),name='vehicule-detail'),
    path('update/<int:pk>/',VehiculeView.as_view(),name='vehicule-update'),
    path('create/',VehiculeView.as_view(),name='vehicule-create'),
    path('delete/<int:pk>/', VehiculeView.as_view(),name='vehicule-delete'),
    path('search/registration/', SearchByRegistrationView.as_view(), name='search_by_registration'),
    path('search/price/', SearchByPriceView.as_view(), name='search_by_price'),


]