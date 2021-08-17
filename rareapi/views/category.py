"""View module for handling requests about posts"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from rareapi.models import Category

class CategoryView(ViewSet):
    """Rare Categories"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized category instance
        """

        category = Category()
        category.label = request.data["label"]

        try:
            category.save()
            serializer = CategorySerializer(category, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single category

        Returns:
            Response -- JSON serialized category instance
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """
        category = Category.objects.get(pk=pk)
        category.label = request.data["label"]
        category.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single category

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            category = Category.objects.get(pk=pk)
            category.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to categorys resource

        Returns:
            Response -- JSON serialized list of categorys
        """

        categorys = Category.objects.all()

        serializer = CategorySerializer(
            categorys, many=True, context={'request': request})
        return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categorys

    Arguments:
        serializer type
    """
    class Meta:
        model = Category
        fields = ('id', 'label')
        depth = 1
