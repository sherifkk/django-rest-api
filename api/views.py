from .models import User
from .serializers import UserSerializer,MessageSerializer
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
        users = User.objects.filter(email=request.POST['email'],password=request.POST['password']);
        if users.exists():
            serializer = UserSerializer(users, many=True)
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

class Users(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users':serializer.data})

class Update(APIView):
    def post(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                    'error'  : False,
                    'message': "Updated successfully",
                    'user'   : serializer.data
            }
            return Response(data)
        return Response(serializer.errors)

class Message(APIView):
    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'error'  : False,
                'message': "Message sent successfully",
                'user'   : serializer.data
            }
            return Response(data)
        return Response(serializer.errors)
