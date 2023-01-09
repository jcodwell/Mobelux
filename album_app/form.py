from django import forms
from .models import Photo,Album

class PhotoForm(forms.ModelForm):
 class Meta:
        model = Photo
        fields = ('image',)


class AlbumForm(forms.ModelForm):
 class Meta:
        model = Album
        fields = ('name','photos',)
