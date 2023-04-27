from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Materia
from .forms import FormMateria, FormEditarMateria, FiltrosMateria
from programas.models import ProgramaAcademico
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect


class Bienvenida(TemplateView):
    template_name = 'home.html'

class ListaMaterias(ListView):
    paginate_by = 5
    model = Materia
    extra_context = {'form': FiltrosMateria}

    
class NuevaMateria(CreateView):
    model = Materia
    form_class = FormMateria
    # fields = '__all__'
    success_url = reverse_lazy('lista_materias')
    extra_context = {'accion': 'Nueva'}
    
    # template_name = 'alta_materia.html'
    # fields = ['nombre','clave','semestre']
    
class EditarMateria(UpdateView):
    model = Materia
    form_class = FormEditarMateria
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_materias')
    
class EliminarMateria(DeleteView):
    model = Materia
    success_url = reverse_lazy('lista_materias')
    
def buscar_materia(request):
    materias = Materia.objects.all().order_by('-nombre','semestre')
    
    if request.method == 'POST':
        
        form = FiltrosMateria(request.POST)
        clave = request.POST.get('clave',None)
        nombre = request.POST.get('nombre',None)
        semestre = request.POST.get('semestre',None)
        creditos = request.POST.get('creditos',None)
        optativa = request.POST.get('optativa',None)
        programa = request.POST.get('programa',None)
        # programa = ProgramaAcademico.objects.get(clave=programa)
        programa2 = request.POST.get('programa2',None)
        
        print(optativa)
        if clave:
            materias = materias.filter(clave=clave)
        if nombre:
            # materias = materias.filter(nombre__startswith=nombre)
            materias = materias.filter(nombre__contains=nombre)
            materias = materias.filter(nombre__icontains=nombre)
            # materias = materias.get(nombre=nombre)
            
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
            
        print(materias.query)
            
    else:
        form = FiltrosMateria()
        
    paginator = Paginator(materias, 5)  # Show 5 contacts per page.
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': form
    } 
    return render(request, 'materias/materia_list.html', context)


def eliminar_todas(request):
    if request.method == 'POST':
        claves = []
        for i in request.POST:
            if i != "csrfmiddlewaretoken":
                claves.append(i)
        if claves:
            Materia.objects.filter(clave__in=claves).delete()
            messages.success(request, 'Materias eliminadas exitosamente.')
    
    return redirect('lista_materias')