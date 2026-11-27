from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render

# Create your views here.
def login(request):
       return render(request, 'web/login.html')



def login(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    error = None
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('login')
        error = 'Usuario o contraseña incorrectos.'

    return render(request, 'web/login.html', {'error': error})

def salir(request):
    auth_logout(request)
    return redirect('login')

@login_required
def inicio(request):
    return render(request, 'web/inicio.html')