from django.urls import path
from . import views

urlpatterns = [
    path('reservas/', views.lista_reservas, name="lista_reservas"),
]