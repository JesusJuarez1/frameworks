from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User, Group
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .token import token_activacion
from django.core.mail import EmailMessage
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from .models import Docente
from .forms import FormDocente, UserForm, FormPerfilDocente
# def login(request):
#     return render(request, 'login.html')



class RegistrarDocente(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'users.permiso_administrador'
    model = Docente
    template_name = 'registrar_docente.html'
    form_class = FormDocente
    success_message = '%(username)s se registró con éxito'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form = UserForm(self.request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # miapp.com
            # localhost:8000
            dominio = get_current_site(self.request)
            mensaje = render_to_string('confirmar_cuenta.html',
                {
                    'user':user,
                    'dominio':dominio,
                    'uid': urlsafe_base64_encode(force_bytes(user.id)),
                    'token': token_activacion.make_token(user)
                }
            )

            email = EmailMessage(
                'Activar cuenta ',
                mensaje,
                to=[user.email]
            )
            email.content_subtype = "html"
            email.send()
        else:
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)

    
    

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    

@login_required
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


class ActivarCuenta(TemplateView):
    def get(self, request, *args, **kwargs):
        # context = self.get_context_data(**kwargs)

        try:
            uid = urlsafe_base64_decode(kwargs['uidb64'])
            token = kwargs['token']
            user = User.objects.get(pk=uid) 
        except(TypeError, ValueError, User.DoesNotExist):
            user = None
        
        if user is not None and token_activacion.check_token(user, token):
            user.is_active = True
            user.save()
            mensaje = 'Cuenta activada, ingresar datos'
        else:
            mensaje = 'Token inválido, contacta al administrador'

        return render(request, "{% url 'login' %}",{'mensaje':mensaje})
        
        # return self.render_to_response(context)
        
@permission_required('users.permiso_administrador')
def lista_usuarios(request):
    usuarios = User.objects.all()
    grupos = Group.objects.all()
    
    context ={
        'usuarios': usuarios,
        'grupos': grupos
    }
    
    return render(request, 'lista_usuarios.html', context)

@permission_required('users.permiso_administrador')
def asignar_grupo_usuarios(request):
    if request.method == 'POST':
        grupo_id = request.POST.get('grupo')
        grupo = Group.objects.get(id=grupo_id)
        ids = []
        for i in request.POST:
            if i != "csrfmiddlewaretoken" and i != "grupo":
                ids.append(i)
        if ids:
            usuarios = User.objects.filter(id__in=ids)
            for usuario in usuarios:
                usuario.groups.add(grupo)
    return redirect('lista_usuarios')