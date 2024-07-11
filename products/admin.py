from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Album, Artist, Genre, Condition

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Album, PostAdmin)
admin.site.register(Genre)
admin.site.register(Condition)
admin.site.register(Artist)



