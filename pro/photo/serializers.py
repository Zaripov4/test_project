from rest_framework import serializers
from .models import Image, Album


class AlbumSerializer(serializers.ModelSerializer):
    image_count = serializers.IntegerField()
    class Meta:
        model = Album
        fields = [
            'title', 
            'id',
            'image_count',
        ]

class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'album',
            'content',
        ]

class ImageListSerializer(ImageCreateSerializer):
    album = AlbumSerializer(many=True, required=False)
