from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

from .models import Docente
from .forms import FormDocente, UserForm, FormPerfilDocente
# def login(request):
#     return render(request, 'login.html')


class RegistrarDocente(SuccessMessageMixin, CreateView):
    model = Docente
    template_name = 'registrar_docente.html'
    form_class = FormDocente
    success_message = '%(username)s se registró con éxito'
    success_url = reverse_lazy('login')
    

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    

def perfil(request):
    # print(request.user.docente)
    try:
        docente = request.user.docente
    except:
        docente = None
    if request.method == 'POST':
        if docente:
            form = FormPerfilDocente(request.POST, request.FILES, instance=docente)
        else:
            form = FormPerfilDocente(request.POST, request.FILES)
        if form.is_valid():
            docente = form.save(commit=False)
            docente.usuario = request.user
            docente.save()
            
            return redirect('bienvenida')
    else:  
        if docente:
            form = FormPerfilDocente(instance=docente)
        else:
            form = FormPerfilDocente()
        
    return render(request, 'perfil_docente.html', {'form':form})
