from rest_framework import serializers
from filmes_app.models import Filme
from .genero_serializer import GeneroSerializer

class FilmeSerializer(serializers.ModelSerializer):
  genero = GeneroSerializer()
  class Meta:
    model = Filme
    fields = '__all__'