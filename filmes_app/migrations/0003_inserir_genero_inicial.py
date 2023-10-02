# Generated by Django 4.2.5 on 2023-10-02 11:07

from django.db import migrations

def inserir_genero_inicial(apps, schema_editor):
  Genero = apps.get_model('filmes_app', 'Genero')
  Genero.objects.create(descricao="Romance")    

class Migration(migrations.Migration):
    dependencies = [
        ("filmes_app", "0002_genero"),
    ]

    operations = [
       migrations.RunPython(inserir_genero_inicial)
    ]
