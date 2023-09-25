from django.urls import path
from .views import FilmeListCreate

urlpatterns = [
  path(
    'filmes/', 
    FilmeListCreate.as_view(), 
    name="filme-list-create"
  )
]