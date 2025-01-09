from django.shortcuts import render

# Create your views here.
def index(request):
    contex= {"mensaje": "Bienvenido a mi aplicación Django"}
    return render(request, "myapp/index.html", contex)