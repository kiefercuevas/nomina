from django.db import models

# Create your models here.


class Ingreso(models.Model):
    Nombre = models.CharField(max_length=100)
    DependeSalario = models.BooleanField(default=True)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return self.Nombre
