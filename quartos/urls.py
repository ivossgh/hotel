from django.urls import path
from . import views

urlpatterns = [
    path('quartos/', views.lista_quartos, name="lista_quartos"),
]