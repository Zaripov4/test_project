from django.db import models

IMAGE_ALBUM = (
    ('Album1', 'Album1'),
    ('Album2', 'Album2'),
    ('Album3', 'Album3'),
    ('Album4', 'Album4'),
    )

class Image(models.Model):
    image_album = models.CharField(
        choices=IMAGE_ALBUM, max_length=20, default='1'
        )
    image_content = models.ImageField(
        upload_to='static/images', default=None
        )