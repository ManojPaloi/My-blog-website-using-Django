from django.urls import path
from . import views

urlpatterns = [
    # Correct URL pattern to match category ID (like /category/1/)
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
]
