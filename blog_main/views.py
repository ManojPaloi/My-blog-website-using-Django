from django.shortcuts import render, redirect
from blogs.models import Category, Blogs
from .forms import RegistrationForm  # ✅ Ensure this matches

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages, auth 
from django.contrib.auth import authenticate

@login_required(login_url='login')
@never_cache
def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured=True, status='published')
    posts = Blogs.objects.filter(is_featured=False, status='published')

    context = {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts
    }
    return render(request, 'home.html', context)






@never_cache
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)  # ✅ Use the correct form name
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  # ✅ Redirect to login after success
    else:
        form = RegistrationForm()  # ✅ Use the correct form name
    
    return render(request, 'register.html', {'form': form})  # ✅ Ensure this template exists







@never_cache
def login(request):  # ✅ Renamed to 'user_login' to avoid conflicts
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, "Login successful! Welcome back.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



@never_cache
def logout(request):
    storage = messages.get_messages(request)
    storage.used = True  # ✅ Clears previous messages before adding a new one

    auth.logout(request)  # ✅ Logs out the user
    messages.success(request, "You have successfully logged out.")  # ✅ Adds a single logout message

    return redirect('login')  # ✅ Redirects to login page