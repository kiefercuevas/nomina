from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Deducion
from Apps.Deduciones.forms.DeduccionesForm import DeduccionesForm 

# Create your views here.

def index(request):
    deduciones = {"Deduciones": Deducion.objects.filter(Estado = True)}
    return render(request, "Deduciones/index.html",deduciones)


def deducionesForm(request, id = 0):

    if request.method == "GET":
        if id == 0:
            form = DeduccionesForm()
        else:
            deduccion = Deducion.objects.get(pk=id)
            if(deduccion.Estado == False):
                return redirect('/Deduciones')
            form = DeduccionesForm(instance=deduccion)
        return render(request, 'Deduciones/create.html', {'form': form })
    else:
        if id == 0:
            form = DeduccionesForm(request.POST)
        else:
            deducion = Deducion.objects.get(pk=id)
            if(deducion.Estado == False):
                return redirect('/Deduciones')
            form = DeduccionesForm(request.POST, instance = deducion)

        if form.is_valid():
            form.save()
            return redirect('/Deduciones')
        else:
            return render(request, 'Deduciones/create.html', {'form': form })




def delete(request, id=0):
    if request.method == "POST":
        if id > 0:
            deducion = Deducion.objects.get(pk=id)
            if(deducion.Estado == False):
                return redirect('/Deduciones')
            deducion.Estado = False
            deducion.save()
            return redirect('/Deduciones')


def getDeduciones(request):
    deducciones = Deducion.objects.filter(Estado = True).values()
    return JsonResponse({"deducciones":list(deducciones)})