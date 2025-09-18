from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'author')

admin.site.register(Post, PostAdmin)
