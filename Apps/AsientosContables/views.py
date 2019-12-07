from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import AsientoContable,Cuenta
from Apps.Transacciones.models import Transaccion
from Apps.Empleados.models import Empleado
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import datetime


def index(request):
    AsientosContables = {"AsientosContables":AsientoContable.objects.all()}
    return render(request, "AsientosContables/index.html",AsientosContables)

def cuentas(request):
    cuentas = {"Cuentas":Cuenta.objects.all()}
    return render(request, "AsientosContables/cuentas.html",cuentas)

@csrf_exempt
def create(request):
    if request.method == 'GET':
        return render(request, "AsientosContables/create.html")
    elif request.method == 'POST':
        resultJson = None
        try:
            AsientoCliente = json.loads(request.body)
            
            for transaction in AsientoCliente['Transacciones']:

                NuevaTransaccion = Transaccion(
                    Empleado = Empleado.objects.get(pk = transaction['Empleado']),
                    Fecha = datetime.datetime.now(),
                    Monto = transaction['Monto'],
                    Estado = True,
                    IDtransacionRegistrada = 0,
                    IngresoDeduccion = transaction['Tipo'],
                    IDingresoDeduccion = transaction['IdIngresoDeduccion'],
                    Descripcion = transaction['Descripcion'],
                    DependeSalario = transaction['DependeSalario'],
                    Moneda = AsientoCliente['Moneda']
                )

                NuevaTransaccion.save()

            resultJson = {'mensaje':'Se ha procesado correctamente','status':200}
        except Exception as e:
            resultJson = {'mensaje':str(e),'status':400}
        
        return JsonResponse(resultJson)



def getCuentas(request):
    cuentas = Cuenta.objects.all().values()
    return JsonResponse({"cuentas":list(cuentas)})


def registrarAsiento(request, id):
    
    # try:
    #     currentAsientoContable = AsientoContable.objects.get(pk = id)
    #     transactions = list(currentAsientoContable.transaccion_set.all().values())

    #     transactionCredit = [ t for t in transactions if t['TipoMovimiento'] == 'CR']
    #     transactionDebit = [ t for t in transactions if t['TipoMovimiento'] == 'DB']
        
    #     CuentaCredito = Cuenta.objects.get(pk = transactionCredit[0]['Cuenta_id'])
    #     CuentaDebito = Cuenta.objects.get(pk = transactionDebit[0]['Cuenta_id'])

    #     totalCredit = sum([t['Monto'] for t in transactionCredit])
    #     totalDebit = sum([t['Monto'] for t in transactionDebit])

    #     newAsiento = {
    #                     "accountingEntryDebit": {
    #                         "description": currentAsientoContable.Descripcion,
    #                         "auxiliaryAccountId": currentAsientoContable.IDauxiliar,
    #                         "account": CuentaDebito.CodigoAuxiliar,
    #                         "movementType": 1,
    #                         "period": currentAsientoContable.FechaAsiento,
    #                         "amount": totalDebit,
    #                         "currencyTypeId": int(currentAsientoContable.Moneda)
    #                     },
    #                     "accountingEntryCredit": {
    #                         "description": currentAsientoContable.Descripcion,
    #                         "auxiliaryAccountId": currentAsientoContable.IDauxiliar,
    #                         "account": CuentaCredito.CodigoAuxiliar,
    #                         "movementType": 1,
    #                         "period": currentAsientoContable.FechaAsiento,
    #                         "amount": totalCredit,
    #                         "currencyTypeId": int(currentAsientoContable.Moneda)
    #                     }
    #                 }

    #     #resultJson['transaction'] = list(transactions)
    #     return JsonResponse({"AsientoContable":newAsiento,"status":200})
    # except Exception as e:
        return JsonResponse({"mensaje":"","status":400})