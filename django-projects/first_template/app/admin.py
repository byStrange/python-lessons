from django.contrib import admin
from .models import Category, Author, Card, Blog, Hash
# Register your models here.

[admin.site.register(model) for model in [Category, Author, Card, Blog, Hash]]
