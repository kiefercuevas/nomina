from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="Transacciones"),
    path('RegistrarTransaccion',views.RegistrarTransaccion,name='RegistrarTransaccion'),
    path('RegistrarIdTransacciones',views.RegistrarIdTransacciones,name='RegistrarIdTransacciones')
]
