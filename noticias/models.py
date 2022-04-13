from django.db import models
from datetime import datetime
from pessoas.models import Pessoa


class Noticia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_noticia = models.CharField(max_length=200)
    escopo = models.TextField()
    referencias = models.TextField()
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    foto_noticia = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)

