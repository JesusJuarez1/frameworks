from django import forms
from .models import Materia, SEMESTRE

class FormMateria(forms.ModelForm):
    
    class Meta:
        model = Materia
        #exclude = ['nombre']
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'clave': forms.TextInput(attrs={'class':'form-control','placeholder':'Clave materia'}),
            'semestre': forms.Select(attrs={'class':'form-control','placeholder':'Semestre'}),
            #'optativa': forms.CheckboxInput(attrs={'class':'form-control','placeholder':'Semestre'}),
            'creditos': forms.NumberInput(attrs={'class':'form-control','placeholder':'Creditos'}),
        }
        
class FormEditarMateria(FormMateria):
    
    class Meta:
        exclude = ['clave']
        model = Materia
        
        
class FiltrosMateria(forms.Form):
    nombre = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder':'Nombre', 'class':'form-control'}),
        required = False,
    )
    clave = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder':'Clave', 'class':'form-control'}),
        required = False,
    )
    semestre = forms.CharField(
        widget = forms.Select(choices=SEMESTRE, attrs={'class':'form-control'}),
        required = False,
    )
    creditos = forms.CharField(
        widget = forms.NumberInput(attrs={'placeholder':'Creditos', 'class':'form-control'}),
        required = False,
    )
    optativa = forms.CharField(
        widget = forms.CheckboxInput(),
        required = False,
    )