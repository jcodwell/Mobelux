

from login_app.views import login_view
from django.urls import path, include

urlpatterns = [
    path('login/', login_view, name='login'),
     path('', include('album_app.urls')),
     
  
]