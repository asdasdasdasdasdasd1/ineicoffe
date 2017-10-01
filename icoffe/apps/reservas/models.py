from django.db import models
from apps.ambientes.models import Ambiente,Mesa

# Create your models here.
class Reserva(models.Model):
    codRes = models.CharField(max_length=10,primary_key=True)
    nomPerRes = models.CharField(max_length=100)
    apePerRes = models.CharField(max_length=100)
    dniPerRes = models.CharField(max_length=8)
    nroPerRes = models.IntegerField(default=1, help_text='Debe incluir a la persona')
    fecRes = models.DateTimeField()
    detalle = models.TextField(blank=True, null=True, default=None)
    mesa = models.ForeignKey(Mesa)
    fecCreRes = models.DateTimeField(auto_now_add=True)
    fecModRes = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codRes