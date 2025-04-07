from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import RegistroForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_superuser:
        return render(request, 'index2.html')
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.rol == 'Administrador':
                return redirect('admin_dashboard')  # Redirigir a la vista de administrador
            elif user.rol == 'Contable':
                return redirect('contable_dashboard')  # Redirigir a la vista de contable
            elif user.rol == 'Técnico':
                return redirect('tecnico_dashboard')  # Redirigir a la vista de técnico
            else:
                return redirect('index')  # Redirigir a la vista de invitado
    return render(request, 'app/login.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de login después de registrar
    else:
        form = RegistroForm()
    
    return render(request, 'app/registro.html', {'form': form})


def acerca(request):
    return render(request, 'acerca.html')

def login(request):
    return render(request, 'login.html')

def clientes(request):
    return render(request, 'mantenimientos/clientes.html')

def productos(request):
    return render(request, 'mantenimientos/productos.html')

def reporte_clientes(request):
    return render(request, 'reportes/clientes_reporte.html')

def logout_view(request):
    logout(request)
    return redirect('index')  

def index2(request):
    return render(request, 'index2.html')

def reporte_productos(request):
    return render(request, 'reportes/productos_reporte.html')

def facturacion(request):
    return render(request, 'procesos/facturacion.html')

def index(request):
    return render(request, 'index.html')

def panel(request):
    return render(request, 'padreIndex.html')

def acerca2(request):
    return render(request, 'acerca2.html')