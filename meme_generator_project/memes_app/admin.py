from django.contrib import admin
from .models import MemeImages
# Register your models here.


@admin.register(MemeImages)
class MemeImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'uid', 'memeImage']
