from album_app.views import *
from django.urls import path, include




urlpatterns = [
 
     path('photo-upload/', upload_photo, name='photo-upload'),
     path('photos/', photo_list, name='photo-list'),
     path('new-album/', new_album, name='album-details'),
     path('albums/', album_list, name='album-list'),
     path(r'^photos/(?P<pk>[0-9]+)/$', photo_remove, name='remove-photo')
   
]