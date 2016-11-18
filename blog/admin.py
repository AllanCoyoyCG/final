from django.contrib import admin
from .models import Libro, LibroAdmin, Usuario, UsuarioAdmin, Prestamo

admin.site.register(Libro,LibroAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Prestamo)
