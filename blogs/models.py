from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category (models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updatrd_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name_plural = 'Categories'

    



    def __str__(self):
        return self.category_name
    



STATUS_CHOICE = (
    ('Draft','Draft'),
    ('published', 'published')
)




    
class Blogs (models.Model):
    title = models.CharField (max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey (User, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to ='uploads/%y/%m/%d')
    short_description = models.TextField(max_length=2000)
    blog_body = models.TextField (max_length=3000)
    status = models.CharField(choices= STATUS_CHOICE, max_length=256, default='Draft')
    is_feacherd = models.BooleanField (default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updatrd_at = models.DateTimeField(auto_now=True)

    

    class Meta:
        verbose_name_plural = 'Blogs'



    def __str__(self):
        return self.title





    

