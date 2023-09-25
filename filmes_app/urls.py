from django.urls import path
from .views import FilmeListCreate, FilmeRetrieveDestroy

urlpatterns = [
  path(
    'filmes/', 
    FilmeListCreate.as_view(), 
    name="filme-list-create"
  ),
  path(
    'filmes/<int:pk>',
    FilmeRetrieveDestroy.as_view(),
    name='filme-retrieve-destroy'
  )
]