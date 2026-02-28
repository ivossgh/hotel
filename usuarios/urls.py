from django.urls import path
from . import views

urlpatterns = [
    path("usuarios/", views.lista_usuarios, name="lista_usuarios"),
]