from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'id','name' , 'email', 'password', 'gender')
        extra_kwargs = {'password': {'write_only': True},'name': {'required': False},'gender': {'required': False}}
