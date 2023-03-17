from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Materia
from .forms import FormMateria, FormEditarMateria, FiltrosMateria
from django import forms
from programas.models import ProgramaAcademico

class ListaMaterias(ListView):
    model = Materia
    extra_context = {'form':FiltrosMateria}
    
class NuevaMateria(CreateView):
    model = Materia
    #fields = '__all__'
    form_class = FormMateria
    extra_context = {'accion': 'Nueva'}
    success_url = reverse_lazy('lista_materias')
    #fields = ['nombre', 'clave', 'semestre', 'creditos']
    #template_name = 'alta_materia.html'
    
class EditarMateria(UpdateView):
    model = Materia
    form_class = FormEditarMateria
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_materias')
    
class EliminarMateria(DeleteView):
    model = Materia
    success_url = reverse_lazy('lista_materias')
    

class Bienvenida(TemplateView):
    template_name = 'home.html'
    

def buscar_materia(request):
    materias = Materia.objects.all().order_by('-nombre','semestre')
    form = FiltrosMateria(request.POST)
    if request.method == 'POST':
        clave = request.POST.get('clave',None)
        nombre = request.POST.get('nombre',None)
        semestre = request.POST.get('semestre',None)
        creditos = request.POST.get('creditos',None)
        programa = request.POST.get('programa',None)
        programa2 = request.POST.get('program',None)
        optativa = request.POST.get('optativa',None)
        # programa = ProgramaAcademico.objects.get(clave=programa)
        
        if clave:
            materias = materias.filter(clave=clave)
        if nombre:
            materias = materias.filter(nombre__contains=nombre)
            # materias = materias.get(nombre=nombre)
            # materias = materias.filter(nombre__startswith=nombre) 
            # Busca cadenas iguales que contengan al comienzo lo que tiene nombre
        if semestre:
            materias = materias.filter(semestre=semestre)
        if creditos:
            materias = materias.filter(creditos=creditos)
        if programa:
            materias = materias.filter(programa__clave=programa)
        if optativa == '1':
            materias = materias.filter(optativa=True)
        elif optativa == '2':
            materias = materias.filter(optativa=False)
        if programa2:
            materias = materias.filter(programa__nombre__contains=programa2)
        ##print(materias.query) Muestra la sentencia sql con la que hace la consulta
    else:
        form = FiltrosMateria()
    context = {
        'object_list':materias,
        'form': form
    }
    return render(request, 'materias/materia_list.html', context)