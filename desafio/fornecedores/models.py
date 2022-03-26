from pyexpat import model
from django.db import models
from django.forms import CharField

class registro(models.Model):
    id = models.CharField(max_length=16)
    name = models.CharField(max_length= 10)
    company = models.CharField(max_length= 30)
    created_at = models.DateField()
    amount_products = models.IntegerField()

    def __str__(self):
        return self.id
