from django.db import models
from django.utils import timezone

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('R', 'Receita'),
        ('D', 'Despesa'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return f'{self.tipo} - {self.valor}'

class Ticker(models.Model):
    nome = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nome
    
class Recibo(models.Model):
    imagem = models.ImageField(upload_to='recibos/')
    data_upload = models.DateTimeField(auto_now_add=True)
    transacao = models.ForeignKey(Transacao, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Recibo {self.id}'
    
# Create your models here.
