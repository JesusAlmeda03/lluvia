from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dash')
        else:
            return redirect('error')
            ##return render(request,'inicio/login.html', {'error': 'Invalid username and password'})

    return render(request, 'inicio/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def dash_view(request):
    return render(request, 'inicio/dash.html')

def mensaje_view(request):
    return HttpResponse(str('Hola Bienvenido'))

def mensajeerror_view(request):
    return HttpResponse(str('Hola Mensaje de error'))
