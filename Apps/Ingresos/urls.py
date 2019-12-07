from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="Ingresos"),
    path('getIngresos', views.getIngresos),
    path('create', views.ingresosForm, name="InsertarIngreso"),  # post and get
    path('create/<int:id>', views.ingresosForm,name="ActualizarIngreso"),
    path('delete/<int:id>', views.delete, name="EliminarIngreso")
]
