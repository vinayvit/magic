from django.db import models
from django.conf import settings
from django.utils import timezone

class Posttop(models.Model):
    titlet = models.TextField()
    textlinkt = models.TextField()
    texttopt = models.TextField()
    textbottmt = models.TextField()
    textt = models.TextField()
    textlinkt = models.TextField()
    linkt = models.TextField()
    ratepointt = models.CharField(max_length = 10)
    linktextbtnt = models.TextField()
    colort = models.CharField(max_length = 50)
    covert = models.ImageField(upload_to = 'images/t/')
    logot = models.ImageField(upload_to = 'images/t/')
	
    def __str__(self):
        return self.titlet

class Posttopsecond(models.Model):
    titles = models.TextField()
    textlinks = models.TextField()
    texttops = models.TextField()
    textbottms = models.TextField()
    texts = models.TextField()
    textlinks = models.TextField()
    links = models.TextField()
    ratepoints = models.CharField(max_length = 10)
    linktextbtns = models.TextField()
    colors = models.CharField(max_length = 50)
    covers = models.ImageField(upload_to = 'images/s/')
    logos = models.ImageField(upload_to = 'images/s/')
	
    def __str__(self):
        return self.titles

class Post(models.Model):
    titlep = models.TextField()
    textlinkp = models.TextField()
    texttopp = models.TextField()
    textbottmp = models.TextField()
    textp = models.TextField()
    textlinkp = models.TextField()
    linkp = models.TextField()
    ratepointp = models.CharField(max_length = 10)
    linktextbtnp = models.TextField()
    colorp = models.CharField(max_length = 50)
    coverp = models.ImageField(upload_to = 'images/p/')
    logop = models.ImageField(upload_to = 'images/p/')
	
    def __str__(self):
        return self.titlep

class Postlive(models.Model):
    titlel = models.TextField()
    textlinkl = models.TextField()
    texttopl = models.TextField()
    textbottml = models.TextField()
    textl = models.TextField()
    textlinkl = models.TextField()
    linkl = models.TextField()
    ratepointl = models.CharField(max_length = 10)
    linktextbtnl = models.TextField()
    colorl = models.CharField(max_length = 50)
    coverl = models.ImageField(upload_to = 'images/l/')
    logol = models.ImageField(upload_to = 'images/l/')
	
    def __str__(self):
        return self.titlel

class Postslot(models.Model):
    titlesl = models.TextField()
    textlinksl = models.TextField()
    texttopsl = models.TextField()
    textbottmsl = models.TextField()
    textsl = models.TextField()
    textlinksl = models.TextField()
    linksl = models.TextField()
    ratepointsl = models.CharField(max_length = 10)
    linktextbtnsl = models.TextField()
    colorsl = models.CharField(max_length = 50)
    coversl = models.ImageField(upload_to = 'images/sl/')
    logosl = models.ImageField(upload_to = 'images/sl/')
	
    def __str__(self):
        return self.titlesl
