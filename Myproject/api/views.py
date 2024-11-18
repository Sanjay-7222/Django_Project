from rest_framework.decorators import api_view
from rest_framework.response import Response
from animania.models import Room,Message
from .serializers import RoomSerializer,MessageSerializer
from rest_framework import status

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET/api',
        'GET/api/messages',
        'GET/api/messages/:id',
    ]
    return Response(routes)

# @api_view(['GET'])
# def getRooms(request):
#     rooms = Room.objects.all()
#     serializer = RoomSerializer(rooms, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    serializers = MessageSerializer(messages, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getMessage(request,id):
    try:
        message = Message.objects.get(id=id)
        serializers = MessageSerializer(message, many=False)
        return Response(serializers.data)
    except Message.DoesNotExist:
        return Response({'error': 'Message was deleted'}, status=status.HTTP_404_NOT_FOUND)