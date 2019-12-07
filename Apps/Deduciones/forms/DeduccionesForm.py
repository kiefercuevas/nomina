from django import forms
from Apps.Deduciones.models import Deducion


class DeduccionesForm(forms.ModelForm):

    class Meta:
        model = Deducion
        fields = ['Nombre','DependeSalario']
        labels = {
            'Nombre': 'Nombre',
            'DependeSalario': 'Depende del salario',
        }

    def __init__(self, *args, **kwargs):
        super(DeduccionesForm, self).__init__(*args, **kwargs)
        self.fields['Nombre'].required = True
        
