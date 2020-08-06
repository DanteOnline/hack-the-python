from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'has_image']


admin.site.register(Post, PostAdmin)
