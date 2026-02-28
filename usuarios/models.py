from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    TIPO_CARGO = [
        ('R','Recepcionista'),
        ('A','Administrador'),
        ('L','Limpeza'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=1, choices=TIPO_CARGO)
    

    def __str__(self):        
        return f'{self.usuario.username} - {self.get_cargo_display()}'
    

    


