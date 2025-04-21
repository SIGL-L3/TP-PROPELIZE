from django.urls import path
from . import views

urlpatterns = [
    path('search/registration/', views.search_by_registration, name='search_by_registration'),
    path('search/price/', views.search_by_price, name='search_by_price'),
]
