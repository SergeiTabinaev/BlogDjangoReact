from django.contrib import admin

from .models import BlogCategory, BlogPost

admin.site.register(BlogPost)
admin.site.register(BlogCategory)
