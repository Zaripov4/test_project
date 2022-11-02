from .models import Image
from rest_framework import viewsets
from .serializers import ImageSerializer
from rest_framework.response import Response

class ImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        params_list = params['pk']
        
        try:
            params_list = int(params_list)
            queryset = Image.objects.get(id=int(params_list))
            serializer = ImageSerializer(queryset)
        
        except:  
            if params_list == 'all':
                queryset = Image.objects.all().order_by('-id')
            else:
                queryset = Image.objects.filter(ImageAlbum=params_list).\
                order_by('-id')
            serializer = ImageSerializer(queryset, many=True)
        
        return Response(serializer.data)