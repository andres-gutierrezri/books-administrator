# biblioteca_ceb/urls.py
from django.contrib import admin
from django.urls import path, include
from libros import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libros.urls')),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


