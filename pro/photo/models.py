from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Image(Album):
    album = models.ManyToManyField(Album, related_name='image_set')
    content = models.ImageField(upload_to='static/images', default=None)
