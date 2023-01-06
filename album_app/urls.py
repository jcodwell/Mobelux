from album_app.views import AlbumViewset
from django.urls import path, include
from rest_framework.routers import SimpleRouter


albumRouter = SimpleRouter()

albumRouter.register(r'albums', AlbumViewset)

urlpatterns = [
    path('', include(albumRouter.urls)),
  
   
]