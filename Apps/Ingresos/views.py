from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Ingreso
from Apps.Ingresos.forms.IngresosForm import IngresosForm 
# Create your views here.


def index(request):
    ingresos = {"Ingresos": Ingreso.objects.filter(Estado = True)}
    return render(request, "Ingresos/index.html",ingresos)

def ingresosForm(request, id = 0):

    if request.method == "GET":
        if id == 0:
            form = IngresosForm()
        else:
            ingreso = Ingreso.objects.get(pk=id)
            if(ingreso.Estado == False):
                return redirect('/Ingresos')
                
            form = IngresosForm(instance=ingreso)
        return render(request, 'Ingresos/create.html', {'form': form })
    else:
        if id == 0:
            form = IngresosForm(request.POST)
        else:
            ingreso = Ingreso.objects.get(pk=id)
            if(ingreso.Estado == False):
                return redirect('/Ingresos')

            form = IngresosForm(request.POST, instance = ingreso)

        if form.is_valid():
            form.save()
            return redirect('/Ingresos')
        else:
            return render(request, 'Ingresos/create.html', {'form': form })




def delete(request, id=0):
    if request.method == "POST":
        if id > 0:
            ingreso = Ingreso.objects.get(pk=id)

            if(ingreso.Estado == False):
                return redirect('/Ingresos')

            ingreso.Estado = False
            ingreso.save()
            return redirect('/Ingresos')

def getIngresos(request):
    ingresos = Ingreso.objects.filter(Estado = True).values()
    return JsonResponse({"ingresos":list(ingresos)})