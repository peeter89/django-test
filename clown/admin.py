from django.contrib import admin
from .models import Author,Hashtag
# Register your models here.


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'date_create')
    list_filter = ('author',)


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('name', 'author', 'description', 'date_create' , 'date_update', 'state', 'display_hashtag')
#     list_filter = ('author',)

# admin.site.register(State)
admin.site.register(Author)

