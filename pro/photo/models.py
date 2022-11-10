from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    @property
    def image_count(self):
        return self.image_set.count()

class Image(models.Model):
    album = models.ManyToManyField(Album, related_name='image_set', blank=True)
    content = models.ImageField(upload_to='static/images', default=None)
