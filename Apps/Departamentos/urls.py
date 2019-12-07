from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="Departamentos"),
    path('create', views.departamentosForm, name="InsertarDepartamento"),  # post and get
    path('create/<int:id>', views.departamentosForm,name="ActualizarDepartamento"),
    path('delete/<int:id>', views.delete, name="EliminarDepartamento")
]
