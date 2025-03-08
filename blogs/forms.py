from django import forms
from .models import Category, Blogs, Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
        }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = [
            'title', 'slug', 'category', 'author', 'blog_image',
            'short_description', 'blog_body', 'status', 'is_featured'
        ]
        labels = {
            'title': 'Blog Title',
            'slug': 'Slug (URL-friendly)',
            'short_description': 'Short Description',
            'blog_body': 'Content',
        }
        help_texts = {
            'slug': 'Enter a unique URL-friendly name for the blog.',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter slug'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'blog_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Short description...'}),
            'blog_body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your blog content here...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write your comment...'}),
        }
