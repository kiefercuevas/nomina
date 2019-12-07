from django.db import models

from Apps.Empleados.models import Empleado
#from Apps.AsientosContables.models import AsientoContable, Cuenta
# Create your models here.


class Transaccion(models.Model):
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    IDingresoDeduccion = models.PositiveIntegerField(default=0)
    Fecha = models.DateTimeField("Fecha de transaccion", auto_now_add=False)
    Monto = models.FloatField()
    Estado = models.BooleanField(default=True)
    IDtransacionRegistrada = models.PositiveIntegerField(default=0)
    IngresoDeduccion = models.CharField(default="", max_length=100)
    DependeSalario = models.BooleanField(default=False)
    Descripcion = models.CharField(default="", max_length=100)
    Moneda = models.CharField(
        choices=[('1', "DOP"), ('2', "Dolar")], max_length=2, default='1')

    def __str__(self):
        return str(self.Fecha)
