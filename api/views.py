from django.shortcuts import render
from rest_framework import viewsets
from .models import user
from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Register(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if user.objects.filter(email=serializer.validated_data['email']).exists():
                data = {
                    'error'  : True,
                    'message': "This email already exist, please login"
                }
            else:
                serializer.save()
                data = {
                    'error'  : False,
                    'message': "Registered successfully",
                    'user'   : serializer.data
                }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
