from django.db import models


class Libro(models.Model):
    ISBN = models.CharField(max_length=20, null=True, blank=True)
    CodigodeBarras = models.CharField(max_length=100, null=True, blank=True)
    NoTopografico = models.CharField(max_length=100, null=True, blank=True)
    Titulo = models.CharField(max_length=255, null=True, blank=True)
    Autor = models.CharField(max_length=200, null=True, blank=True)
    Ciudad = models.CharField(max_length=100, null=True, blank=True)
    Editorial = models.CharField(max_length=100, null=True, blank=True)
    Fecha = models.CharField(max_length=50, null=True, blank=True)
    Edicion = models.CharField(max_length=50, null=True, blank=True)
    Pagsovols = models.CharField(max_length=20, null=True, blank=True)
    Ejemplares = models.CharField(max_length=20, null=True, blank=True)
    Genero = models.CharField(max_length=50, null=True, blank=True)
    Ubicacion = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.Titulo
