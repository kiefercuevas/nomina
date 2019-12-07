from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Transaccion
from Apps.Empleados.models import Empleado
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    transacciones = {"Transacciones":Transaccion.objects.all()}
    return render(request, "Transacciones/index.html",transacciones)

@csrf_exempt
def RegistrarTransaccion(request):

    transactionsId = json.loads(request.body)
    descripcion = None
    Fecha = datetime.datetime.now()
    totalDebito = 0
    totalCredito = 0
    Moneda = None
    t = None
    for transactionId in transactionsId["transactionIds"]:
        CurrentTransaction = Transaccion.objects.get(pk = int(transactionId))
        SueldoEmpleado = CurrentTransaction.Empleado.SalarioMensual
        t = CurrentTransaction.Moneda

        if(descripcion == None):
            descripcion = CurrentTransaction.Descripcion 

        if(Moneda == None):
            Moneda = CurrentTransaction.Moneda

        if(CurrentTransaction.IngresoDeduccion == "ingreso"):
            if(CurrentTransaction.DependeSalario):
                SueldoEmpleado += int((SueldoEmpleado * (CurrentTransaction.Monto / 100)))
            else:
                SueldoEmpleado += int(CurrentTransaction.Monto)
        else:
            if(CurrentTransaction.DependeSalario):
                SueldoEmpleado -= int((SueldoEmpleado * (CurrentTransaction.Monto / 100)))
            else:
                SueldoEmpleado -= int(CurrentTransaction.Monto)

        totalDebito = SueldoEmpleado
        totalCredito = SueldoEmpleado

    newAsiento = {
                    "accountingEntryDebit": {
                        "description": descripcion,
                        "auxiliaryAccountId": 2,
                        "account": 71,
                        "movementType": 1,
                        "period": Fecha,
                        "amount": totalDebito,
                        "currencyTypeId": int(Moneda)
                    },
                    "accountingEntryCredit": {
                        "description": descripcion,
                        "auxiliaryAccountId": 2,
                        "account": 70,
                        "movementType": 1,
                        "period": Fecha,
                        "amount": totalCredito,
                        "currencyTypeId": int(Moneda)
                    }
                }

    return JsonResponse({"Asiento":newAsiento,"status":200,"message":"ok"}) 


@csrf_exempt
def RegistrarIdTransacciones(request):

    transactions = json.loads(request.body)
    newId = transactions["IDtransacionRegistrada"]
    idTransacciones = transactions['transactionIds']

    for transactionId in idTransacciones:
        CurrentTransaction = Transaccion.objects.get(pk = int(transactionId))
        CurrentTransaction.IDtransacionRegistrada = newId
        CurrentTransaction.save()
    
    return JsonResponse({"status":200,"message":"Transacciones registradas correctamente"}) 