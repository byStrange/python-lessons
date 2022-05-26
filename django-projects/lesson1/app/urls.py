from django.urls import path
from .views import __json, HomeView

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('quiz_json/', __json, name='quiz_json'),
]