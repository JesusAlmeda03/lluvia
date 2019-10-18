from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request,'inicio/login.html', {'error': 'Invalid username and password'})

    return render(request, 'inicio/login.html')