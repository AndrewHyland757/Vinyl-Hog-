from django.contrib import admin
from .models import Album, Artist, Genre, Condition

# Register your models here.

admin.site.register(Genre)
admin.site.register(Condition)
admin.site.register(Album)
admin.site.register(Artist)
