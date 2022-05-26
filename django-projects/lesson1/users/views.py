from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/', {'message': 'You are already logged in'})
    if request.method == 'POST':
        print('not authenticated')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

# we don't need register_user()

# def register_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#         user = User.objects.create_user(username=username, password=password)
#         user.save()
#         return redirect('/', {'success', 'User created successfully'})
#     return render(request, 'register.html')