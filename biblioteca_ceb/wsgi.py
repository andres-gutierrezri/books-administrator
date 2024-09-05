# myproject/wsgi.py
import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.sessions.models import Session

# Elimina todas las sesiones al iniciar
Session.objects.all().delete()

application = get_wsgi_application()

