from django.shortcuts import render, redirect
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogPostForm
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import never_cache



# Create your views here.
@login_required(login_url='login')
@never_cache
def dashboard (request):
    category_counts = Category.objects.all().count()
    blogs_counts = Blogs.objects.all().count()
    
    context = {
        'category_counts': category_counts,
        'blogs_counts': blogs_counts
    }
    return render (request,'dashboard/dashboard.html', context)




@login_required(login_url='login')
@never_cache
def categories (request):
    context = {
        'category_counts': Category.objects.all().count()
    }
    return render (request, 'dashboard/categories.html', context)






@login_required(login_url='login')
@never_cache
def add_categories (request):
    if request.method=='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form':form
    }
    return render (request, 'dashboard/add_categories.html',context )


@login_required(login_url='login')
@never_cache
def edit_categories (request, pk):
    category= get_object_or_404(Category, pk=pk)
    if request.method=='POST':
        form=CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect ('categories')
    form= CategoryForm(instance=category)
    context={
        'form':form,
        'category':category
    }
    return render (request, 'dashboard/edit_categories.html', context )




@login_required(login_url='login')
@never_cache
def delete_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories') 





@login_required(login_url='login')
@never_cache

def posts (request):
    
    posts= Blogs.objects.all()
    context={
        'posts': posts
    }
    return render (request, 'dashboard/posts.html',context)




@login_required(login_url='login')
@never_cache
def add_posts(request):
    form = BlogPostForm()  # ✅ Ensures 'form' is always defined, even for GET requests

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)  # ✅ Re-initialize form for POST data
        if form.is_valid():
            form.save()
            print ("Success")
            return redirect('posts')  # ✅ Ensure 'posts' is a valid name in urls.py

    context = {
        'form': form  # ✅ Always pass 'form' to the template
    }
    return render(request, 'dashboard/add_posts.html', context)







@login_required(login_url='login')
@never_cache
def edit_posts(request, pk):
    post = get_object_or_404(Blogs, pk=pk)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')  # ✅ Redirect to 'posts' page after updating

    else:
        form = BlogPostForm(instance=post)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'dashboard/edit_posts.html', context)








@login_required(login_url='login')
@never_cache


def delete_posts(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    
    post.delete()
    return redirect('posts')  # Redirect to 'posts' view after deletion

  

