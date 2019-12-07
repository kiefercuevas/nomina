from django import forms
from Apps.Puestos.models import Puesto


class PuestosForm(forms.ModelForm):

    class Meta:
        model = Puesto
        fields = ['Descripcion']
        labels = {
            'Descripcion': 'Descripcion',
        }

    def __init__(self, *args, **kwargs):
        super(PuestosForm, self).__init__(*args, **kwargs)
        self.fields['Descripcion'].required = True
