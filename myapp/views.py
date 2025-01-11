from django.shortcuts import render, redirect
from .forms import EstudianteForm, ProfesorForm  # Importar formulario desde forms.py
from .models import Estudiante, Profesor  # Importar modelo desde models.py
from django.db.models import Q
#==================================INDEX====================================================
def index(request):
    return render(request, 'myapp/index.html')


#==================================ESTUDIANTE=CARGA ESTUDIANTE====================================================
def cargar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
            return redirect('index')
    else:
        form = EstudianteForm()
    return render(request, 'myapp/estudiante_form.html', {'form': form})

#==================================LISTA===ESTUDIANTE=====================================================
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/lista_estudiantes.html', {'estudiantes': estudiantes})

#==================================PROFESOR====================================================
def cargar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_profesores')
        else:
            # Agregamos la depuración para capturar errores del formulario
            print("Errores en el formulario:", form.errors)
    else:
        form = ProfesorForm()
    return render(request, 'myapp/profesor_form.html', {'form': form})


def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'myapp/lista_profesores.html', {'profesores': profesores})

# =============================BUSQUEDA=================================================
def buscar(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        estudiantes = Estudiante.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(correo=query)
        )
        profesores = Profesor.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(correo=query) | Q(profesion__icontains=query) | Q(direccion__icontains=query)
        )

        for estudiante in estudiantes:
            resultados.append({
                'tipo': 'Estudiante',
                'nombre': estudiante.nombre,
                'apellido': estudiante.apellido,
                'correo': estudiante.correo,
                'extra': '-',
            })

        for profesor in profesores:
            resultados.append({
                'tipo': 'Profesor',
                'nombre': profesor.nombre,
                'apellido': profesor.apellido,
                'correo': profesor.correo,
                'extra': f'{profesor.profesion} / {profesor.direccion}',
            })

    return render(request, 'myapp/index.html', {'resultados': resultados})