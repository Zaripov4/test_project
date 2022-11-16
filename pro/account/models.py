from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import ValidationError


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_on_isnull=True)


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_on = models.DateTimeField(auto_now=True, db_index=True)
    deleted_on = models.DateTimeField(null=True, blank=True, default=None)

    objects = BaseManager()
    objects_all = models.Manager()

    class Meta:
        abstract = True
        ordering = ['created_on']

    def mark_deleted(self):
        self.deleted_on = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class CustomManager(UserManager):
    def create_user(self, username, password, **extra_fields):
        if not all([username, password]):
            raise ValidationError(
                {'detail': 'Required fields: username, password'}
            )
        user = self.model(
            username=username,
            password=password,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, *args, **kwargs):
        user = self.create_user(password=password, *args, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser, BaseModel):
    id = models.AutoField(editable=False, primary_key=True)
    username = models.CharField(_('username'), max_length=128, unique=True)
    password = models.CharField(_('password'), max_length=256)
    email = models.EmailField(_('email address'), null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']
    objects = CustomManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
