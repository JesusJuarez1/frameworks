from django import forms
from .models import Horario

class FormHorario(forms.ModelForm):
    
    class Meta:
        model = Horario
        fields = '__all__'
        # fields = ['clave, nombre']
        
        widgets = {
            'clave': forms.TextInput(attrs={'class':'form-control','placeholder':'Clave'}),
            'semestre': forms.Select(attrs={'class':'form-control','placeholder':'Semestre'}),
            'dia': forms.Select(attrs={'class':'form-control','placeholder':'Dia'}),
            'hora': forms.TextInput(attrs={'class':'form-control','placeholder':'Hora'}),
        }

class FormEditarHorario(FormHorario):
    class Meta:
        exclude = ['clave']
        model = Horario
        
