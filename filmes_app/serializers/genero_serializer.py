from rest_framework import serializers
from filmes_app.models import Genero
class GeneroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genero
    fields = '__all__'