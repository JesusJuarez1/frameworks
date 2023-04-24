from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Horario
from .forms import FormHorario, FormEditarHorario
from django import forms

class ListaHorarios(ListView):
    paginate_by = 5
    model = Horario
    
class NuevoHorario(CreateView):
    model = Horario
    form_class = FormHorario
    extra_context = {'accion': 'Nuevo'}
    success_url = reverse_lazy('lista_horarios')
    
class EditarHorario(UpdateView):
    model = Horario
    form_class = FormEditarHorario
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_horarios')
    
class EliminarHorario(DeleteView):
    model = Horario
    success_url = reverse_lazy('lista_horarios')