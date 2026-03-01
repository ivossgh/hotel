from django.shortcuts import render
from reservas.models import Reserva

def lista_reservas(request):
    reservas = Reserva.objects.all()
    context = {
        'reservas':reservas
    }
    return render(request, 'lista_reservas.html', context)