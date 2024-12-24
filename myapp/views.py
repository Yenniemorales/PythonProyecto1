from django.shortcuts import render

def index(request):
    context = {'mensaje': '¡Bienvenido a mi aplicacion Django!'}  # Esto es un diccionario correcto
    return render(request, 'myapp/index.html', context)
