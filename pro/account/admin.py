from curses.ascii import US
from re import U
from django.contrib import admin
from account.models import User

admin.site.register(User)