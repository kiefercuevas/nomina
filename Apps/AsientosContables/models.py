from django.db import models
from Apps.Empleados.models import Empleado

# Create your models here.


class AsientoContable(models.Model):

    Descripcion = models.CharField(max_length=100)
    FechaAsiento = models.DateTimeField(auto_now_add=True)
    Estado = models.CharField(choices=[(
        "R", "Registrado"), ("P", "Pendiente")], max_length=2, default='P')
    IDauxiliar = models.PositiveIntegerField(default=2)
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Moneda = models.CharField(
        choices=[('1', "DOP"), ('2', "Dolar")], max_length=2, default='1')

    def __str__(self):
        return self.Descripcion


class Cuenta(models.Model):
    Descripcion = models.CharField(max_length=100)
    Monto = models.FloatField()
    CodigoAuxiliar = models.PositiveIntegerField(default=0)
    NaturalezaCuenta = models.CharField(
        choices=[("DB", "Debito"), ("CR", "Credito")], max_length=2, default='DB')

    def __str__(self):
        return self.Descripcion
