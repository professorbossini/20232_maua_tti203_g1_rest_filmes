from rest_framework import serializers
from .models import Filme
from .models import Genero

class GeneroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genero
    fields = '__all__'

class FilmeSerializer(serializers.ModelSerializer):
  genero = GeneroSerializer()
  class Meta:
    model = Filme
    fields = '__all__'

