from django.contrib import admin
from .models import Blogs, Category, Comment

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status', 'is_featured', 'created_at')
    search_fields = ('title', 'short_description', 'blog_body')
    list_filter = ('status', 'category', 'is_featured')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'created_at')
