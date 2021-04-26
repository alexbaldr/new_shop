from django.contrib import admin
from main.models import (Publishers, Authors, Genres, Books, Comments, Like)

@admin.register(Publishers)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id','name', ]

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'slug']


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Genres._meta.get_fields()]
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'info']

@admin.register(Comments)
class ComentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'text']

# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ['id']