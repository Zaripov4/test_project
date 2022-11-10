from rest_framework import serializers
from .models import Image, Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class AlbumListSerializer(AlbumSerializer):
    image_count = serializers.SerializerMethodField()

    def get_image_count(self, obj):
        return obj.image_set.count()


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ImageListSerializer(ImageCreateSerializer):
    album = AlbumSerializer(many=True, required=False)
