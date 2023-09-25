from django.shortcuts import render
from rest_framework import generics
from .models import Filme
from .serializers import FilmeSerializer
# Create your views here.
# POST /filmes {"titulo"...}
# 1. Qual é a tabela em que o objeto será armazenado
# 2. QUal é a classe serializadora

#filmes/1
# GET /Filmes
# 1. Qual é a tabela de onde os dados virão
# 2. Qual é a classe serializadora
class FilmeListCreate(generics.ListCreateAPIView):
  queryset = Filme.objects.all()
  serializer_class = FilmeSerializer
