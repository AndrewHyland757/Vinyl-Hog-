from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Album, Artist, Genre, Condition

# Register your models here.

class AlbumAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    ordering = ['title']

admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre)
admin.site.register(Condition)
admin.site.register(Artist)



