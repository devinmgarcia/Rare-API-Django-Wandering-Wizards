"""View module for handling requests about authors"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rareapi.models import Author
from django.contrib.auth.models import User


class AuthorView(ViewSet):
    """Rare Authors"""

    def list(self, request):
        """Handle GET requests to authors resource
        
        Returns JSON serialized list of authors
        """
        authors = Author.objects.all()
        serializer = AuthorSerializer(
            authors, many=True, context={'request': request})
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff']

class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer"""
    user = UserSerializer(many=False)

    class Meta:
        model = Author
        fields = ['id', 'user', 'profile_image_url', 'created_on', 'active']
