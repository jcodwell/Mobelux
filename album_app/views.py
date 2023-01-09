
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Photo,Album
from album_app.form import AlbumForm, PhotoForm

def upload_photo(request):
    if request.method == "POST":
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.title = request.FILES['image'].name
            post.save()
            return redirect('photo-list')
        return render(request, 'photo.html', {'form': form})
    else:
  
        form = PhotoForm(request.POST, request.FILES)
        return render(request, 'photo.html', {'form': form})
     

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo-list.html', {'photos': photos})
 

def new_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST,request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form._save_m2m()
            return redirect('album-list')
        return render(request, 'album.html', {'form': form})
    else:
        form = AlbumForm(request.POST, request.FILES)
        return render(request, 'album.html', {'form': form})
       

def album_list(request):
        albums = Album.objects.all
        return render(request, 'album-list.html', {'albums': albums}) 