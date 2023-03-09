from django.shortcuts import render

def hola(request):
    return render(request, 'hola.html')

def saludo(request, id):
    nombre = 'Jesus'
    edad = 22
    materias = ['Linux',
                'Álgebra',
                'Administración de proyectos',
                'Arqui']
    calificaciones = [
        {'mat':'Linux', 'cal':9},
        {'mat':'Álgebra', 'cal':10},
        {'mat':'Administración de proyectos', 'cal':8},
        {'mat':'Arqui', 'cal':7}
    ]
    otro_id = id if id else 0
    context = {
        'nombre': nombre,
        'edad': edad,
        'materias': materias,
        'calificaciones': calificaciones,
        'id': otro_id
    }
    return render(request, 'saludo.html', context)
