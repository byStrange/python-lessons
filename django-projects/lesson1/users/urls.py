from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [ 
    path('login/', views.login_user, name='login'),
]