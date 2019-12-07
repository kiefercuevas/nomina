from django import forms
from Apps.Departamentos.models import Departamento


class DepartamentosForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = ['Descripcion']
        labels = {
            'Descripcion': 'Descripcion',
        }

    def __init__(self, *args, **kwargs):
        super(DepartamentosForm, self).__init__(*args, **kwargs)
        self.fields['Descripcion'].required = True
