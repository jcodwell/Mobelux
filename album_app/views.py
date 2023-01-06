from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet
from .serializers import AlbumSerializer
from .models import Album

class AlbumViewset(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    template_name = 'album.html'
