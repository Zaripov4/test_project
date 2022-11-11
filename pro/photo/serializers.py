from rest_framework import serializers
from .models import Image, Album

class ImageMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('content', )


class AlbumSerializer(serializers.ModelSerializer):
    image_count = serializers.IntegerField()
    image_view = ImageMinimalSerializer(many=True)
    class Meta:
        model = Album
        fields = [
            'title', 
            'id',
            'image_count',
            'image_view',
        ]


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title')


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'album',
            'content',
        ]

class ImageListSerializer(ImageCreateSerializer):
    album = AlbumListSerializer(many=True, required=False)
