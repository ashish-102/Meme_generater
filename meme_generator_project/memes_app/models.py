from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MemeImages(models.Model):
    """
    store edited image on db sqlite
    """
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    memeImage = models.ImageField(upload_to='media/')
