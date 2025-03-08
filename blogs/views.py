from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.db.models import Q
from .models import Blogs, Category, Comment
from .forms import CommentForm


@login_required(login_url='login')
@never_cache
def posts_by_category(request, category_id):
    posts = Blogs.objects.filter(status='published', category_id=category_id)
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)




@login_required(login_url='login')
@never_cache
def blogs(request, slug):
    print(f"🔍 Debug: Requested Slug - {slug}")

    single_post = get_object_or_404(Blogs, slug=slug, status__iexact='Published')
    print(f"✅ Found Blog: {single_post.title}")

    comments = Comment.objects.filter(blog=single_post).order_by('-created_at')
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.blog = single_post
                comment.user = request.user

                parent_id = request.POST.get("parent")
                if parent_id:
                    try:
                        parent_comment = Comment.objects.get(id=parent_id)
                        comment.parent = parent_comment
                    except Comment.DoesNotExist:
                        messages.error(request, "Parent comment not found.")
                        return redirect('blog_detail', slug=slug)

                comment.save()
                messages.success(request, "Comment posted successfully!")
                return redirect('blog_detail', slug=slug)
            else:
                messages.error(request, "You must be logged in to comment.")
                return redirect('login')

    context = {
        'single_post': single_post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blogs.html', context)




@login_required(login_url='login')
@never_cache
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user or request.user.is_staff:
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
        return redirect('blog_detail', slug=comment.blog.slug)

    messages.error(request, "You are not authorized to delete this comment.")
    return redirect('home')

@login_required(login_url='login')
def search(request):
    keyword = request.GET.get('keyword', '').strip()  # Ensure keyword is not None
    blogs = Blogs.objects.none()  # Default empty queryset

    if keyword:
        blogs = Blogs.objects.filter(
            Q(title__icontains=keyword) | 
            Q(short_description__icontains=keyword) | 
            Q(blog_body__icontains=keyword), 
            status='published'
        )

    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', context)
