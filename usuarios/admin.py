from django.contrib import admin

from .models import Cliente, Quarto, Reserva

admin.site.register(Cliente)
admin.site.register(Quarto)
admin.site.register(Reserva)

