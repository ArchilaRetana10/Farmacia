from django.urls import path
from . import views
from .views import registro

urlpatterns = [
    # Ruta principal
    path('', views.index, name='index'),
    path('7', views.index2, name='index2'),  # Página con el mensaje de bienvenida

    
    # Submódulo Acerca 
    path('acerca/', views.acerca, name='acerca'),
    path('acerca2/', views.acerca2, name='acerca2'),

    
    # Submódulo Login
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', registro, name='registro'),


    # Submódulo Mantenimientos
    path('mantenimientos/clientes/', views.clientes, name='clientes'),
    path('mantenimientos/productos/', views.productos, name='productos'),

    # Submódulo Reportes
    path('reportes/clientes/', views.reporte_clientes, name='reporte_clientes'),
    path('reportes/productos/', views.reporte_productos, name='reporte_productos'),
    
    # Submódulo Procesos
    path('procesos/facturacion/', views.facturacion, name='facturacion'),

    # Ruta para el panel de administración
    path('panel/', views.panel, name='panel'),
]
