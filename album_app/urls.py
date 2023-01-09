from album_app.views import upload_photo, photo_list,new_album,album_list
from django.urls import path, include



urlpatterns = [
 
     path('photo-upload/', upload_photo, name='photo-upload'),
     path('photos/', photo_list, name='photo-list'),
     path('new-album/', new_album, name='album-details'),
     path('albums/', album_list, name='album-list'),
   
]