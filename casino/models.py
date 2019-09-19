from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    title = models.TextField()
    textlink = models.TextField()
    texttop = models.TextField()
    textbottm = models.TextField()
    text = models.TextField()
    textlink = models.TextField()
    link = models.TextField()
    ratepoint = models.CharField(max_length = 10)
    linktextbtn = models.TextField()
    color = models.CharField(max_length = 50)
    cover = models.ImageField(upload_to = 'images/p/')
    logo = models.ImageField(upload_to = 'images/p/')
	
    def __str__(self):
        return self.titlep

