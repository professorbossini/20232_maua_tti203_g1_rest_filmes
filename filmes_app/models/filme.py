from django.db import models
from .genero import Genero
class Filme(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField()
  diretor = models.CharField(max_length=100)
  genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

  def __str__(self):
    return self.titulo