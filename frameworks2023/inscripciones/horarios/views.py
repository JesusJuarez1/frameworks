from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Horario
from .forms import FormHorario, FormEditarHorario
from django import forms

class ListaHorarios(LoginRequiredMixin, ListView):
    paginate_by = 5
    model = Horario
    
class NuevoHorario(PermissionRequiredMixin, CreateView):
    permission_required = ['docentes.permiso_docente','users.permiso_administrador']
    model = Horario
    form_class = FormHorario
    extra_context = {'accion': 'Nuevo'}
    success_url = reverse_lazy('lista_horarios')
    
class EditarHorario(PermissionRequiredMixin, UpdateView):
    permission_required = ['docentes.permiso_docente','users.permiso_administrador']
    model = Horario
    form_class = FormEditarHorario
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_horarios')
    
class EliminarHorario(PermissionRequiredMixin, DeleteView):
    permission_required = ['docentes.permiso_docente','users.permiso_administrador']
    model = Horario
    success_url = reverse_lazy('lista_horarios')