from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('product/', views.product, name='product'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('support/', views.support, name='support'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('docs/', views.docs, name='docs'),
]
