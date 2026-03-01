from django.shortcuts import render
from quartos.models import Quarto

def lista_quartos(request):
    quartos = Quarto.objects.all()
    context = {'quartos':quartos}
    return render(request, 'lista_quartos.html', context)