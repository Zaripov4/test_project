from .models import Image, Album
from rest_framework import viewsets
from .serializers import ImageCreateSerializer, AlbumSerializer, ImageListSerializer, AlbumListSerializer

class ImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()

    def get_serializer_class(self):
        self.serializer_class = ImageListSerializer
        if self.action in ['create', 'update', 'partial_update']:
            self.serializer_class = ImageCreateSerializer
        return super().get_serializer_class()


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
    def get_serializer_class(self):
        self.serializer_class = AlbumListSerializer
        if self.action == 'create':
            self.serializer_class = AlbumSerializer

        return super().get_serializer_class()

