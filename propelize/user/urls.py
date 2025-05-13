from django.urls import  path
from .views import UserView

urlpatterns = [
    path('user/create',UserView.as_view(),name='create-user'),
    path('user/update',UserView.as_view(),name='update-user'),
]