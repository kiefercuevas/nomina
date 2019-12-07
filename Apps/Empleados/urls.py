from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="Empleados"),
    path('getEmpleados',views.getEmpleados),
    path('create', views.empleadosForm, name="InsertarEmpleado"),  # post and get
    path('create/<int:id>', views.empleadosForm,name="ActualizarEmpleado"),
    path('delete/<int:id>', views.delete, name="EliminarEmpleado")
]
