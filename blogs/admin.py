from django.contrib import admin
from django.db import models
from.models import Category, Blogs

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updatrd_at')

admin.site.register(Category, CategoryAdmin)



class BlogAdmin (admin.ModelAdmin):
    blog_body = models.TextField (max_length=3000)
    list_display = ('id', 'title', 'slug', 'Category', 'author', 'blog_image','short_description', 'blog_body','status','is_feacherd','created_at','updatrd_at')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_feacherd',)




admin.site.register(Blogs,BlogAdmin)