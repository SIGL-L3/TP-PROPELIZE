from django.urls import path
from .views import SearchByRegistrationView, SearchByPriceView

urlpatterns = [
    path('search/registration/', SearchByRegistrationView.as_view(), name='search_by_registration'),
    path('search/price/', SearchByPriceView.as_view(), name='search_by_price'),
]
