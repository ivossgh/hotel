from django.db import models # criar as tabelas do banco de dados, precisamos dela 
from django.contrib.auth.models import User # para criar a tabela de funcionários, que é uma extensão da tabela de usuários do Django

# Minha tabela clientes no banco
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)

    # para exibir o nome do cliente ao invés do id no admin
    def __str__(self):
        return self.nome

# Minha tabela funcionario no banco
class Funcionario(models.Model):
    # Caixinha de selecao
    TIPO_CARGO = [
        ('R','Recepcionista'),
        ('A','Administrador'),
        ('L','Limpeza'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=1, choices=TIPO_CARGO)
    
# Mostro o nome e o cargo do funcionário no admin, ao invés do id
    def __str__(self):        
        return f'{self.usuario.username} - {self.get_cargo_display()}'
    

    


