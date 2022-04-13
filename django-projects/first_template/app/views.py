from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def product(request):
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact.html')

def support(request):
    return render(request, 'support.html')

def about(request):
    return render(request, 'about.html')

def docs(request):
    return render(request, 'documentation.html')