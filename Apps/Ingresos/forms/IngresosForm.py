from django import forms
from Apps.Ingresos.models import Ingreso


class IngresosForm(forms.ModelForm):

    class Meta:
        model = Ingreso
        fields = ['Nombre','DependeSalario']
        labels = {
            'Nombre': 'Nombre',
            'DependeSalario': 'Depende del salario',
        }

    def __init__(self, *args, **kwargs):
        super(IngresosForm, self).__init__(*args, **kwargs)
        self.fields['Nombre'].required = True
