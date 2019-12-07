from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="Deduciones"),
    path('getDeduciones', views.getDeduciones),
    path('create', views.deducionesForm, name="InsertarDeducion"),  # post and get
    path('create/<int:id>', views.deducionesForm,name="ActualizarDeducion"),
    path('delete/<int:id>', views.delete, name="EliminarDeduccion")
]
