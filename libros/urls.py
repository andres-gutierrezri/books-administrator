# libros/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('libros/', views.lista_libros, name='lista_libros'),  # Esta ruta maneja la lista de libros
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('libros/info/', views.libros, name='libros'),  # Cambio de la ruta para evitar duplicidad
    path('guardar_libro/', views.guardar_libro, name='guardar_libro'),
    path('libros/editar/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
]



