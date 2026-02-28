from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    #path('quartos/', include('quartos.urls')),
    #path('reservas/', include('reservas.urls')),
]
