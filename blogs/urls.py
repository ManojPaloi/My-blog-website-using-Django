from django.urls import path
from . import views  # ✅ Importing views module

urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('blogs/<slug:slug>/', views.blogs, name='blog_detail'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),  # ✅ Fix: Call from views
]
