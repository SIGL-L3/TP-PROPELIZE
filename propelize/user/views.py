from rest_framework.views import  APIView
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User

class UserView(APIView):

    def post(self,request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    def patch(self,request,pk):
        user = get_object_or_404(User,pk=pk)

        serializer = UserSerializer(user,request.data,partial=True)

        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
