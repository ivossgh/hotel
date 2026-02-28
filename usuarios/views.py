from django.shortcuts import render # necessario para mostrar a página para o usuário
from usuarios.models import Cliente # Precisamos puxar para consegirmos acessar a tabela de clientes

# nossa funcao que url de listar vai pegar. 
# Nosso request é o pedido do usuário para acessar a página, 
# e a gente vai pegar os clientes do banco de dados e mandar para o template
def lista_usuarios(request):
    # Puxamos todos os clientes do banco de dados e alocamos na variavel usuario
    usuarios = Cliente.objects.all()
    # Criamos um dicionário de contexto para mandar os clientes para o html depois
    context = {'usuarios': usuarios}

    # Renderizamos a página lista_usuarios.html, passando o contexto com os clientes para o html
    return render(request, 'lista_usuarios.html', context)


