from django.db import models
from django.utils import timezone
from django.contrib import admin

class Libro(models.Model):
    isbn    = models.CharField(max_length=13)
    titulo    = models.CharField(max_length=40)
##  Portada    = models.CharField(upload_to='portada/imagen', null=True,blank=True )
    autor    = models.CharField(max_length=50)
    editorial   = models.CharField(max_length=50)
    anio    = models.IntegerField()

    def __str__(self):
        return self.isbn


class Usuario(models.Model):
    nombre   = models.CharField(max_length=60)
    dpi     = models.CharField(max_length=40)
    libros   = models.ManyToManyField(Libro, through='Prestamo')
    def __str__(self):
        return self.nombre

class Prestamo (models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(blank=True, null=True)
    fecha_devolucion_propuesta = models.DateTimeField(blank=True, null=True)
    fecha_devolucion_real = models.DateTimeField(blank=True, null=True)

class PrestamoInLine(admin.TabularInline):
    model = Prestamo
    extra = 1


class LibroAdmin(admin.ModelAdmin):
    inlines = (PrestamoInLine,)


class UsuarioAdmin (admin.ModelAdmin):
    inlines = (PrestamoInLine,)
