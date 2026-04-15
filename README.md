📝 Descripción
  Este proyecto es un módulo centralizado de autenticación y autorización desarrollado para un sistema de farmacia. El objetivo principal es restringir y otorgar acceso a diferentes áreas del sistema basándose en perfiles de usuario específicos. 
  El sistema utiliza una lógica de RBAC (Role-Based Access Control) para asegurar que solo el personal autorizado, pueda realizar acciones críticas como la modificación de inventarios o la visualización de reportes financieros.

🚀 Tecnologías utilizadas
  Backend: Python, Django Framework.
  Frontend: HTML5, CSS.
  Base de Datos: PostgreSQL.
  Seguridad: Sistema de autenticación nativo de Django.

🔐 Características de Seguridad
  Jerarquía de Roles: Definición de múltiples tipos de usuarios con permisos granulares.
  Interfaz Dinámica: El menú y las opciones de la interfaz de usuario cambian en tiempo real según los permisos del usuario logueado.

🛠️ Instalación y Configuración
  Clonar el repositorio:
    git clone https://github.com/ArchilaRetana10/Farmacia.git
    cd Farmacia
    python -m venv venv

  # En Windows (Git Bash):
  source venv/Scripts/activate
  # En Windows (CMD):
  venv\Scripts\activate

  pip install django

python manage.py makemigrations app
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

