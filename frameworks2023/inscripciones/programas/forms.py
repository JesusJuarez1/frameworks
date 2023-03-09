from django import forms
from programas.models import ProgramaAcademico

class FormProgramaAcademico(forms.ModelForm):
    
    class Meta:
        model = ProgramaAcademico
        fields = '__all__' # ['clave', 'nombre']