from django.db import models

# Create your models here.

class Songs(models.Model):
    song = models.CharField("Name of The Song:",max_length=20)
    artist = models.CharField("Artist:",max_length=20)
    comments = models.TextField("Your View on the Song:")
