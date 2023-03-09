from django.shortcuts import render

def mensaje(request):
    return render(request, 'app2/mensaje.html')

def hola(request):
    return render(request, 'app2/hola.html')
