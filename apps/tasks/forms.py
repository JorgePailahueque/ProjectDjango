from django import forms
from apps.tasks.models import Task

class FormTask(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            # first call parent's constructor
            super(FormTask, self).__init__(*args, **kwargs)
            # there's a `fields` property now
    class Meta:
        model = Task

        fields = [
            'id',
            'nombre',
            'des',
            'fecha_ini',
            'fecha_fin',
            'asignado',
            'status',
            'resources',

        ]

        labels = {
            'id' : 'ID',
            'nombre': 'Nombre',
            'des' : 'Descripcion',
            'fecha_ini': 'Fecha inicio (usar formato AAAA-MM-DD)',
            'fecha_fin': 'Fecha fin (usar formato AAAA-MM-DD)',
            'asignado' : 'Asignado',
            'status' : 'Estado',
            'resources' : 'Resources',
        }

        widgets = {
            'id' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'des' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ini' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_fin' : forms.TextInput(attrs={'class':'form-control'}),
            'asignado' : forms.SelectMultiple(attrs={'class' : 'form-control'}),
            'status' : forms.SelectMultiple(attrs={'class' : 'form-control'}),
            'resources': forms.CheckboxSelectMultiple(),
        }