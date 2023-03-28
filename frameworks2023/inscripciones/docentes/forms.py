from django import forms
from .models import Docente
from django.urls import reverse_lazy

class FormDocente(forms.ModelForm):
    
    class Meta:
        model = Docente
        fields = '__all__'
        exclude = ['usuario']
        
        widgets = {
            'estado' : forms.Select(attrs={
                'class':'form-control',
                'data-url': reverse_lazy('busca_municipios')
                }),
        }