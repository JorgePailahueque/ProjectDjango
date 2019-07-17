from django import forms
from apps.projects.models import Project

class AddProjects(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            # first call parent's constructor
            super(AddProjects, self).__init__(*args, **kwargs)
            # there's a `fields` property now
            self.fields['participantes'].required = False
    class Meta:
        model = Project

        fields = [
            'id',
            'nombre',
            'fecha_ini',
            'fecha_fin',
            'participantes',

        ]

        labels = {
            'id' : 'ID',
            'nombre': 'Nombre',
            'fecha_ini': 'Fecha inicio (usar formato AAAA-MM-DD)',
            'fecha_fin': 'Fecha fin (usar formato AAAA-MM-DD)',
            'participantes': 'Participantes',
        }

        widgets = {
            'id' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ini' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_fin' : forms.TextInput(attrs={'class':'form-control'}),
            'participantes': forms.CheckboxSelectMultiple(),
        }