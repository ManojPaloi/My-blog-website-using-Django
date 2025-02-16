from django.shortcuts import render, redirect
from blogs.models import Category,Blogs
from .forms import RegistrationForm  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache






@login_required(login_url='login')
@never_cache
def home(request):
    
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_feacherd = True, status='published')
    posts= Blogs.objects.filter(is_feacherd = False, status='published')

    context = {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts
    }
    return render(request, 'home.html', context)








def register (request):
    if request.method== "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('register')
    else:
        form = RegistrationForm()
    context= {

        'form':form

    }


    return render (request, 'register.html', context)







def login (request):
    if request.method=="POST":
        form= AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect ('dashboard')
    else:
        form = AuthenticationForm()

    context = {
        'form':form
    }
    return render (request, 'login.html', context)




@login_required(login_url='login')
@never_cache
def logout (request):
    auth.logout(request)
    return redirect ('home')