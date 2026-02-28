from django.db import models
from usuarios.models import Cliente
from quartos.models import Quarto 

class Reserva(models.Model):
    STATUS_RESERVA = [
        ('P', 'Pendente'),
        ('C', 'Confirmada'),
        ('F', 'Finalizada'),
    ]

    usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    data_check_in = models.DateField()
    data_check_out = models.DateField()
    valor_reserva = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_RESERVA, default='Pendente')
    data_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reserva de {self.usuario.nome} para o quarto {self.quarto.numero} - Status: {self.get_status_display()}'
