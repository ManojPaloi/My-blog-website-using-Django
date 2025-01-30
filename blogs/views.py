from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from .models import Blogs, Category
from django.db.models import Q

def posts_by_category(request, category_id):
    posts = Blogs.objects.filter(status='published', Category_id=category_id)
    category = get_object_or_404(Category, pk=category_id)  # Renamed to 'category'
    context = {
        'posts': posts,
        'category': category  # Pass as 'category' to the template
    }
    return render(request, 'posts_by_category.html', context)




def blogs (request, slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='published')
    context={
        'single_post':single_post

    } 
    
    return render (request,'blogs.html',context)




def search (request):
    keyword= request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
    content={
        'blogs':blogs,
        'keyword':keyword
    }
    return render (request, 'search,html',content)