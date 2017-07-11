from rest_framework import serializers
from .models import user

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ( 'id','name' , 'email', 'password', 'gender')
        extra_kwargs = {'password': {'write_only': True}}
