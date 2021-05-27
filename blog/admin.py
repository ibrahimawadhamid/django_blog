from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'author', 'created_at', 'updated_at')
    readonly_fields = ['created_at', 'updated_at']
    list_display = ('title', 'author', 'created_at')


admin.site.register(Post, PostAdmin)
