from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='', blank=False)
    some = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(default='', max_length=100)
    user_image = models.ImageField(upload_to='author_images', blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField( auto_now_add=True)
    username = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'

class Hash(models.Model):
    hash_name = models.CharField(max_length=100)
    def __str__(self):
        return self.hash_name

class Card(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CharField)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'card'
        verbose_name_plural = 'cards'

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    hash_tag = models.ManyToManyField('Hash')
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post_little_img = models.ImageField(upload_to='blog_images/60x60/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
