from rest_framework import serializers
from .models import User,Message

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model        = User
        fields       = ('id', 'name' , 'email', 'password', 'gender')
        extra_kwargs = {'password': {'write_only': True}}

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id','from','to','title','message','sent')
        extra_kwargs = {'from': {'source': 'from_users_id'}, 'to': {'source': 'to_users_id'},  'sent': {'source': 'sentat', 'read_only': True}}
