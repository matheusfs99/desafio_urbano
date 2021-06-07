from django.db import models

# Create your models here.

class Planilha(models.Model):
    nome = models.CharField("Nome", max_length=100)
    cliente = models.CharField("Cliente", max_length=100)
    arquivo = models.FileField("Arquivo (.csv)", upload_to='uploads/')
