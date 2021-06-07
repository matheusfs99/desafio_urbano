from django.db import models

# Create your models here.

class Processo(models.Model):
    pasta = models.CharField("Pasta", max_length=100)
    comarca = models.CharField("Comarca", max_length=100)
    uf = models.CharField("UF", max_length=100)
