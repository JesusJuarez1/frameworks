from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,permission_required
from unidades_academicas.models import UnidadAcademica
from unidades_academicas.forms import FormUnidadAcademica
from django.core.paginator import Paginator

@login_required
def lista_unidades(request):
    unidades = UnidadAcademica.objects.all().order_by('nombre')
    paginator = Paginator(unidades,5)  # Show 5 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'unidades' : unidades
    }
    return render(request, 'lista_unidades.html', context)


@permission_required('users.permiso_administrador')
def nueva_unidad(request):
    if request.method == 'POST':
        form = FormUnidadAcademica(request.POST) #Llena con lo que trae el post el formulario
        if form.is_valid(): #Valida los datos
            form.save() #Guarda en la base de datos
            return redirect('lista_unidades')
        
    else:
        form = FormUnidadAcademica()
    
    context = {
        'form' : form
    }
    return render(request, 'nueva_unidad.html', context)


@permission_required('users.permiso_administrador')
def eliminar_unidad(request, id):
    UnidadAcademica.objects.get(id=id).delete()
    return redirect('lista_unidades')


@permission_required('users.permiso_administrador')
def editar_unidad(request, id):
    unidad = UnidadAcademica.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormUnidadAcademica(request.POST, instance=unidad) #Llena con lo que trae el post el formulario
        if form.is_valid(): #Valida los datos
            form.save() #Guarda en la base de datos
            return redirect('lista_unidades')
        
    else:
        form = FormUnidadAcademica(instance=unidad)
    
    context = {
        'form' : form
    }
    return render(request, 'editar_unidad.html', context)