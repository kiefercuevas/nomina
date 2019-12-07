from django.db import models
from Apps.Departamentos.models import Departamento
from Apps.Puestos.models import Puesto
from django.core.validators import MinLengthValidator
# Create your models here.


class Empleado(models.Model):
    Cedula = models.CharField(
        validators=[MinLengthValidator(11)], max_length=11, unique=True)
    Nombre = models.CharField(max_length=50)
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    SalarioMensual = models.FloatField()
    EstadoEmp = models.BooleanField(default=True)

    def __str__(self):
        return self.Nombre
