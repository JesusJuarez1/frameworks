from django.shortcuts import render

def login(request):
    mensaje = None
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        mensaje = "Usuario no válido"
        if username == 'jesus' and password == '123456':
            mensaje = f"Bienvenido al sistema {username}"
            return render(request, 'home.html', {'mensaje':mensaje})
        
    return render(request, 'login.html', {'mensaje':mensaje})