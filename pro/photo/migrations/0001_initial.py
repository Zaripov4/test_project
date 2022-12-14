# Generated by Django 4.1.2 on 2022-11-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('content', models.ImageField(
                    default=None,
                    upload_to='static/images')),
                ('album', models.ManyToManyField(
                    related_name='image_set',
                    to='photo.album')),
            ],
        ),
    ]
