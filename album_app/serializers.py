

from rest_framework import serializers

from album_app.models import Album

class PhotoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    image = serializers.ImageField()
   

class AlbumSerializer(serializers.Serializer):
    name = serializers.EmailField()
    photos = PhotoSerializer(many=True)

  