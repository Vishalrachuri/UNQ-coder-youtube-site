from django.db import models
import os
from django.conf import settings


# Create your models here.
class PlayList(models.Model):
    playname = models.CharField(max_length=100, primary_key=True)
    desc = models.TextField()
    img = models.ImageField(upload_to=os.path.join(settings.BASE_DIR, 'media'))
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.playname


class Viedo(models.Model):
    Vname = models.CharField(max_length=100, primary_key=True)
    desc = models.TextField()
    playname = models.ForeignKey(PlayList, on_delete=models.CASCADE)
    iframelink = models.CharField(max_length=100)
    vedioNumber = models.IntegerField()
    istop = models.BooleanField(default=False)
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.Vname
