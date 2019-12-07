from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="Puestos"),
    path('create', views.puestosForm, name="InsertarPuesto"),  # post and get
    path('create/<int:id>', views.puestosForm,name="ActualizarPuesto"),
    path('delete/<int:id>', views.delete, name="EliminarPuesto")
]
