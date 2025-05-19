from django.urls import  path
from .views import UserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('create/',UserView.as_view(),name='create-user'),
    path('update/<int:pk>/',UserView.as_view(),name='update-user'),
    path('login/', TokenObtainPairView.as_view(),name='token_obtain'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh')
]