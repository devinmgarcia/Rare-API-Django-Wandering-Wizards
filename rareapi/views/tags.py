"""View module for handling requests about posts"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rareapi.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for event host's related Django user"""
    class Meta:
        model = Tag
        fields = ('id', 'label')


class TagView(ViewSet):
    """Level up posts"""

    def list(self, request):
        """Handle GET requests to posts resource

        Returns:
            Response -- JSON serialized list of posts
        """
        # Get all tags from the database
        tags = Tag.objects.all()

        tag_type = self.request.query_params.get('type', None)
        if tag_type is not None:
            tags = tags.filter(tag_type_id=tag_type)

        serializer = TagSerializer(
            tags, many=True, context={'request': request})
        return Response(serializer.data)

