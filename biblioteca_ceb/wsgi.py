import os
from django.core.wsgi import get_wsgi_application

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_ceb.settings')

# Inicializar la aplicación WSGI de Django
application = get_wsgi_application()

# Importar el modelo después de la inicialización
from django.contrib.sessions.models import Session

# Eliminar todas las sesiones al iniciar
Session.objects.all().delete()

