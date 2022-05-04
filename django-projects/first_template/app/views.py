from django.shortcuts import render
from .models import Card, Blog
# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def product(request):
    cards = Card.objects.all()
    context = {
        'cards': cards
    }
    return render(request, 'product.html', context)

def product_detail(request, slug):
    card = Card.objects.get(slug=slug)
    context = {
        'card': card
    }
    return render(request, 'product-details.html', context)

def contact(request):
    return render(request, 'contact.html')

def support(request):
    return render(request, 'support.html')

def about(request):
    return render(request, 'about.html')

def docs(request):
    return render(request, 'documentation.html')