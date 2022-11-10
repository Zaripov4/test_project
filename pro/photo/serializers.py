from rest_framework import serializers
from .models import Image, Album


class AlbumSerializer(serializers.ModelSerializer):
    image_count = serializers.IntegerField()
    class Meta:
        model = Album
        fields = '__all__'

class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ImageListSerializer(ImageCreateSerializer):
    album = AlbumSerializer(many=True, required=False)
