from django.shortcuts import render
from usuarios.models import Cliente

def lista_usuarios(request):
    usuarios = Cliente.objects.all()
    context = {'usuarios': usuarios}

    return render(request, 'lista_usuarios.html', context)


