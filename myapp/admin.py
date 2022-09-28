from django.contrib import admin
from .models import Page, Post, Song
# Register your models here.

@admin.register(Page)
class pageAdmin(admin.ModelAdmin):
    list_display= ['page_name', 'page_cat', 'page_pub_date', 'user']


@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display= ['post_name', 'post_cat', 'post_pub_date', 'user']


@admin.register(Song)
class songAdmin(admin.ModelAdmin):
    list_display= ['song_name', 'song_duration', 'song_pub_date', 'written_by']