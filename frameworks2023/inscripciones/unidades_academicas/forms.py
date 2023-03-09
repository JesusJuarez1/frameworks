from django import forms
from unidades_academicas.models import UnidadAcademica

class FormUnidadAcademica(forms.ModelForm):
    
    class Meta:
        model = UnidadAcademica
        fields = '__all__'
        