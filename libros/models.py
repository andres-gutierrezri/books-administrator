from django.db import models


class Libro(models.Model):
    ISBN = models.CharField(max_length=13)
    CodigodeBarras = models.CharField(max_length=100)
    NoTopografico = models.CharField(max_length=100)
    Titulo = models.CharField(max_length=200)
    Autor = models.CharField(max_length=200)
    Ciudad = models.CharField(max_length=100)
    Editorial = models.CharField(max_length=100)
    Fecha = models.DateField()
    Edicion = models.CharField(max_length=50)
    Pagsovols = models.IntegerField()
    Ejemplares = models.IntegerField()
    Genero = models.CharField(max_length=100)
    Ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.Titulo
