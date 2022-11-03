from email.policy import default
from pyexpat import model
from tkinter.messagebox import NO
from tokenize import blank_re
from django.db import models

class Album(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    date_created = models.DateTimeField(blank=True)
    last_updated = models.DateTimeField(blank=True)

class Image(models.Model):
    image = models.ManyToManyField(Album)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    image_content = models.ImageField(upload_to='static/images', default=None)