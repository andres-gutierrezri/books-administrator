from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Libro
from .forms import LibroForm


@login_required
def home(request):
    return render(request, "libros/home.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Credenciales inválidas. Inténtelo de nuevo.")
    return render(request, "libros/login.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect("home")


@login_required
def nosotros(request):
    # Lógica para la vista de "nosotros"
    return render(request, "libros/nosotros.html")


@login_required
def lista_libros(request):
    libros = Libro.objects.all()  # Obtén todos los libros de la base de datos
    paginator = Paginator(libros, 100)  # 100 registros por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "libros/libros.html", {"libros": page_obj})


@login_required
def guardar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_libros")
    else:
        form = LibroForm()
    return render(request, "libros/libros.html", {"form": form})


@login_required
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect("lista_libros")
    else:
        form = LibroForm(instance=libro)
    return render(request, "libros/editar_libro.html", {"form": form})


@login_required
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    libro.delete()
    return redirect("lista_libros")


@login_required
def libros(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_libros")
    else:
        form = LibroForm()

    libros = Libro.objects.all()  # Obtén todos los libros de la base de datos
    paginator = Paginator(libros, 100)  # 100 registros por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "libros/libros.html", {"form": form, "libros": page_obj})
