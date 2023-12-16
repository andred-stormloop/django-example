# messages/views.py
from rest_framework import generics
from .models import Message
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import MessageSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Message
from .serializers import MessageSerializer

@method_decorator(csrf_exempt, name='dispatch')

class MessageDeleteView(APIView):

    def delete(self, request, pk):
        try:
            message = Message.objects.get(pk=pk)
        except Message.DoesNotExist:
            return Response({'error': 'Message not found or you do not have permission to delete it.'}, status=status.HTTP_404_NOT_FOUND)

        message.delete()
        return Response({'message': 'Message deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        message_id = self.kwargs.get('message_id')
        message = Message.objects.get(pk=message_id)
        serializer.save()
        message.comments.add(serializer.instance)
        message.save()

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    
class MessageListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MessageUpvoteView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.upvotes += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)