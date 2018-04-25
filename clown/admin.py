from django.contrib import admin
from .models import Author,Hashtag
# Register your models here.


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'date_create')
    list_filter = ('author',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name' , 'last_name', 'date_of_birth', 'date_create')