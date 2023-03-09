from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Materia
from .forms import FormMateria, FormEditarMateria, FiltrosMateria
from django import forms

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
    
class EliminarrMateria(DeleteView):
    model = Materia
    success_url = reverse_lazy('lista_materias')
    

class Bienvenida(TemplateView):
    template_name = 'home.html'
    

def buscar_materia(request):
    materias = Materia.objects.all()
    form = FormMateria(request.POST)
    if request.method == 'POST':
        clave = request.POST.get('clave',None)
        nombre = request.POST.get('nombre',None)
        semestre = request.POST.get('semestre',None)
        creditos = request.POST.get('creditos',None)
        optativa = request.POST.get('optativa',None)
        
        if clave:
            materias = materias.filter(clave=clave)
        if nombre:
            materias = materias.filter(nombre=nombre)
        if semestre:
            materias = materias.filter(semestre=semestre)
        if creditos:
            materias = materias.filter(creditos=creditos)
        if optativa:
            materias = materias.filter(optativa=optativa)
    context = {
        'object_list':materias,
        'form': form
    }
    return render(request, 'materias/materia_list.html', context)