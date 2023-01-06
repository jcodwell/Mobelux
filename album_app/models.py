from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    title =   models.CharField(max_length=256, null=False)
    image = models.ImageField(upload_to='img', null = True)

class Album(models.Model):
  name = models.CharField(max_length=256, null=False)
  photos = models.ManyToManyField(Photo) 
  user = models.ForeignKey(User, on_delete=models.CASCADE)