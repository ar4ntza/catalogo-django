from django.contrib import admin

from .models import Cancion, Playlist

admin.site.register(Cancion)
admin.site.register(Playlist)