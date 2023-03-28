from django.shortcuts import render
from .models import Docente, Municipio
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FormDocente

class ListaDocente(ListView):
    model = Docente
    extra_context = {'form':FormDocente}

class NuevoDocente(CreateView):
    model = Docente
    #fields = '__all__'
    form_class = FormDocente
    extra_context = {'accion': 'Nuevo'}
    success_url = reverse_lazy('lista_docentes')


def busca_municipios(rquest):
    id_estado = rquest.POST.get('id_estado', None)
    if id_estado:
        municipios = Municipio.objects.filter(estado_id=id_estado)
        data = [{'id':mun.id, 'nombre':mun.nombre} for mun in municipios]
        return JsonResponse(data, safe=False)
    return JsonResponse({'Error':'Parámetro inválido'}, safe=False)