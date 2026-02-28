from django.contrib import admin

from .models import Cliente
from quartos.models import Quarto
from reservas.models import Reserva

admin.site.register(Cliente)
admin.site.register(Quarto)
admin.site.register(Reserva)

