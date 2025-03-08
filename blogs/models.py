from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Fixed typo

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


STATUS_CHOICE = (
    ('Draft', 'Draft'),
    ('Published', 'Published')  # Consistent casing
)

class Blogs(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Fixed field name
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='uploads/%Y/%m/%d')  # Fixed upload format
    short_description = models.TextField(max_length=2000)
    blog_body = models.TextField(max_length=3000)
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default='Draft')
    is_featured = models.BooleanField(default=False)  # Fixed field name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Fixed typo

    class Meta:
        verbose_name_plural = 'Blogs'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Blogs.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug  # Assign unique slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Comment(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # ✅ Allow anonymous users
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username if self.user else "Anonymous"} on {self.blog.title}'


