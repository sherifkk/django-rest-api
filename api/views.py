from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class Register(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=serializer.validated_data['email']).exists():
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
            return Response(data)
        return Response(serializer.errors)

class Login(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=serializer.validated_data['email'],password=serializer.validated_data['password']);
            if user.exists():
                data = {
                    'error'  : False,
                    'message': "User has been authenticated successfully",
                    'user'   : serializer.data
                }

            else:
                data = {
                    'error'  : True,
                    'message': "Invalid email or password"
                }
            return Response(data)
        return Response(serializer.errors)
