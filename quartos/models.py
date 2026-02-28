from django.db import models

class Quarto(models.Model):
    QUARTO_TIPO = [
        ('S', 'Solteiro'),
        ('C', 'Casal'),
        ('F', 'Familia'),
    ]

    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=1, choices=QUARTO_TIPO)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    descricao = models.TextField()
    # QUando cadastrar um quarto a imagem la vai ser salva na nossa pasta media
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return f'Quarto {self.numero} - {self.get_tipo_display()}'
