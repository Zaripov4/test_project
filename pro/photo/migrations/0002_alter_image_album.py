# Generated by Django 4.1.2 on 2022-11-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='album',
            field=models.ManyToManyField(blank=True, related_name='image_set', to='photo.album'),
        ),
    ]
