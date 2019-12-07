from django.db import models

# Create your models here.


class Puesto(models.Model):
    Descripcion = models.CharField(max_length=100)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return self.Descripcion
