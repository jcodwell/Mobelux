from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from album_app.views import AlbumViewset

def login_view(request):
    """
    Login Function View using the built-in Django Admin Page . 
  
    Parameters:
    request (HTTPRequest): A Reqeust from a Post Call
  
    Returns:
    Render of the Next View
  
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('albums/')
        else:
            # Invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
