from django.shortcuts import render, redirect
from .models import Room

# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html')

def check_view(request):
    room = request.GET.get('room_name')
    username = request.GET.get('username')
    if Room.objects.filter(title=room).exists():
        return redirect('/' + room + "/?name=" + username, room=room)
        