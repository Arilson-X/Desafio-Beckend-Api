from http.client import LENGTH_REQUIRED
from pyexpat import model
from django.db import models
from django.forms import CharField

class RegistroFornecedores(models.Model):
    id = models.CharField(max_length=16,primary_key=True,help_text= "Use o formato TESTE000001TESTE, onde 1 é para o identificacao 1")
    name = models.CharField(max_length= 10)
    company = models.CharField(max_length= 30)
    created_at = models.DateField()
    amount_products = models.IntegerField()

    def __str__(self):
        return self.id
