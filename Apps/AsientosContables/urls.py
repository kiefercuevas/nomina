from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="AsientosContables"),
    path('create',views.create,name="CrearAsiento"),
    path('cuentas', views.cuentas, name="Cuentas"),
    path('getCuentas',views.getCuentas),
    path('registrarAsiento/<int:id>',views.registrarAsiento)
]
