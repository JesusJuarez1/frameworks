from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from programas.models import ProgramaAcademico
from programas.forms import FormProgramaAcademico
from django.core.paginator import Paginator


@login_required
def lista_programas(request):
    programas = ProgramaAcademico.objects.all().order_by('nombre')
    paginator = Paginator(programas,5)  # Show 5 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'programas' : programas
    }
    return render(request, 'lista_programas.html', context)

@permission_required('users.permiso_administrador')
def nuevo_programa(request):
    if request.method == 'POST':
        form = FormProgramaAcademico(request.POST) #Llena con lo que trae el post el formulario
        if form.is_valid(): #Valida los datos
            form.save() #Guarda en la base de datos
            return redirect('lista_programas')
        
    else:
        form = FormProgramaAcademico()
    
    context = {
        'form' : form
    }
    return render(request, 'nuevo_programa.html', context)


@permission_required('users.permiso_administrador')
def eliminar_programa(request, clave):
    ProgramaAcademico.objects.get(clave=clave).delete()
    return redirect('lista_programas')


@permission_required('users.permiso_administrador')
def editar_programa(request, clave):
    programa = ProgramaAcademico.objects.get(clave=clave)
    
    if request.method == 'POST':
        form = FormProgramaAcademico(request.POST, instance=programa) #Llena con lo que trae el post el formulario
        if form.is_valid(): #Valida los datos
            form.save() #Guarda en la base de datos
            return redirect('lista_programas')
        
    else:
        form = FormProgramaAcademico(instance=programa)
    
    context = {
        'form' : form
    }
    return render(request, 'editar_programa.html', context)
