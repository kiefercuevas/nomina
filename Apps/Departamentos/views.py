from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Departamento
from Apps.Empleados.models import Empleado
from Apps.Departamentos.forms.DepartamentosForm import DepartamentosForm
# Create your views here.


def index(request):
    departamentos = {"Departamentos": Departamento.objects.filter(Estado=True)}
    return render(request, "Departamentos/index.html", departamentos)


def departamentosForm(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = DepartamentosForm()
        else:
            departamento = Departamento.objects.get(pk=id)
            if(departamento.Estado == False):
                return redirect('/Departamentos')

            form = DepartamentosForm(instance=departamento)
        return render(request, 'Departamentos/create.html', {'form': form})
    else:
        if id == 0:
            form = DepartamentosForm(request.POST)
        else:
            departamento = Departamento.objects.get(pk=id)
            if(departamento.Estado == False):
                return redirect('/Departamentos')
            form = DepartamentosForm(request.POST, instance=departamento)

        if form.is_valid():
            form.save()
            return redirect('/Departamentos')
        else:
            return render(request, 'Departamentos/create.html', {'form': form})


def delete(request, id=0):
    if request.method == "POST":
        if id > 0:
            departamento = Departamento.objects.get(pk=id)

            if(departamento.Estado == False):
                return redirect('/Departamentos')

            departamento.Estado = False
            empleados = Empleado.objects.filter(Departamento_id=departamento)

            for empleado in empleados:
                empleado.EstadoEmp = False
                empleado.save()

            departamento.save()
            return redirect('/Departamentos')
