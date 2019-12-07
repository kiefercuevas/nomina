from django import forms
from Apps.Empleados.models import Empleado
from Apps.Departamentos.models import Departamento
from Apps.Puestos.models import Puesto


def ValidateCedula(param):
    cedulaException = ['00000000018', '11111111123', '00100759932', '00105606543', '00114272360', '00200123640',
                       '00200409772', '00800106971', '01200004166', '01400074875', '01400000282', '03103749672', '03200066940',
                       '03800032522', '03900192284', '04900026260', '05900072869', '07700009346', '00114532330', '03121982479',
                       '40200700675', '40200639953', '00121581750', '00119161853', '22321581834', '00121581800', '09421581768',
                       '22721581818', '90001200901', '00301200901', '40200452735', '40200401324', '10621581792']

    invalidCedulas = ['00000000000']

    param = str(param)

    if not param.isnumeric():
        return False

    if not len(param) == 11:
        return False

    if param in cedulaException:
        return True

    if param in invalidCedulas:
        return False

    verificatorDigit = int(param[-1:])
    length = len(param) - 1
    weitght = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0
    division = 0
    result = 0

    for i in range(length):
        mult = int(param[i]) * weitght[i]
        if mult < 10:
            total += mult
        else:
            mult = str(mult)
            total += int(mult[:1]) + int(mult[1])

    division = total % 10
    if (division != 0):
        result = 10 - division
    else:
        result = 0

    if result == verificatorDigit:
        return True
    else:
        return False


class EmpleadosForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ['Nombre', 'SalarioMensual',
                  'Cedula', 'Departamento', 'Puesto']
        labels = {
            'Nombre': 'Nombre',
            'SalarioMensual': 'Salario Mensual',
        }
        error_messages = {
            'Cedula': {
                'unique': "La cedula ya esta registrada"
            }
        }

    def __init__(self, *args, **kwargs):
        super(EmpleadosForm, self).__init__(*args, **kwargs)
        self.fields['Nombre'].required = True
        self.fields['Cedula'].required = True
        self.fields['SalarioMensual'].required = True
        self.fields['Departamento'].queryset = Departamento.objects.filter(
            Estado=True)
        self.fields['Puesto'].queryset = Puesto.objects.filter(Estado=True)
        self.fields['Departamento'].empty_label = "Selecciona un departamento"
        self.fields['Puesto'].empty_label = "Selecciona un puesto"

    def clean(self):
        super(EmpleadosForm, self).clean()

        Cedula = self.cleaned_data.get('Cedula')

        if not ValidateCedula(Cedula):
            self._errors['Cedula'] = self.error_class([
                'La cedula no es valida'])

        return self.cleaned_data
