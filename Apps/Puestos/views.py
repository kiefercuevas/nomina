from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Puesto
from Apps.Empleados.models import Empleado
from Apps.Puestos.forms.PuestosForm import PuestosForm
# Create your views here.


def index(request):
    puestos = {"Puestos": Puesto.objects.filter(Estado=True)}
    return render(request, "Puestos/index.html", puestos)


def puestosForm(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = PuestosForm()
        else:
            puesto = Puesto.objects.get(pk=id)
            if(puesto.Estado == False):
                return redirect('/Puestos')

            form = PuestosForm(instance=puesto)
        return render(request, 'Puestos/create.html', {'form': form})
    else:
        if id == 0:
            form = PuestosForm(request.POST)
        else:
            puesto = Puesto.objects.get(pk=id)
            if(puesto.Estado == False):
                return redirect('/Puestos')

            form = PuestosForm(request.POST, instance=puesto)

        if form.is_valid():
            form.save()
            return redirect('/Puestos')
        else:
            return render(request, 'Puestos/create.html', {'form': form})


def delete(request, id=0):
    if request.method == "POST":
        if id > 0:
            puesto = Puesto.objects.get(pk=id)

            if(puesto.Estado == False):
                return redirect('/Puestos')

            puesto.Estado = False
            empleados = Empleado.objects.filter(Puesto_id=puesto)
            for empleado in empleados:
                empleado.EstadoEmp = False
                empleado.save()

            puesto.save()
            return redirect('/Puestos')
