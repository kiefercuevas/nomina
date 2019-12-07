from django.contrib import admin
from .models import AsientoContable,Cuenta

# Register your models here.

models = AsientoContable, Cuenta
admin.site.register(models)