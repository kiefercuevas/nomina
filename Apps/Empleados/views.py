from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Empleado
from Apps.Empleados.forms.EmpleadosForm import EmpleadosForm
# Create your views here.


def index(request):
    empleados = {"Empleados": Empleado.objects.filter(EstadoEmp=True)}
    return render(request, "Empleados/index.html", empleados)


def empleadosForm(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmpleadosForm()
        else:
            empleado = Empleado.objects.get(pk=id)
            if(empleado.EstadoEmp == False):
                return redirect('/Empleados')
            form = EmpleadosForm(instance=empleado)
        return render(request, 'Empleados/create.html', {'form': form})
    else:
        if id == 0:
            form = EmpleadosForm(request.POST)
        else:
            empleado = Empleado.objects.get(pk=id)
            if(empleado.EstadoEmp == False):
                return redirect('/Empleados')
            form = EmpleadosForm(request.POST, instance=empleado)

        if form.is_valid():
            form.save()
            return redirect('/Empleados')
        else:
            return render(request, 'Empleados/create.html', {'form': form})


def delete(request, id=0):
    if request.method == "POST":
        if id > 0:
            empleado = Empleado.objects.get(pk=id)
            if(empleado.EstadoEmp == False):
                return redirect('/Empleados')

            empleado.EstadoEmp = False
            empleado.save()
            return redirect('/Empleados')


def getEmpleados(request):
    empleados = Empleado.objects.filter(EstadoEmp=True).values()
    return JsonResponse({"empleados": list(empleados)})
