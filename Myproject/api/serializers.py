from rest_framework.serializers import ModelSerializer
from animania.models import Room,Message
from rest_framework import serializers

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    room_name = serializers.CharField(source='room.name', read_only=True)
    class Meta:
        model = Message
        fields = '__all__'