from django.shortcuts import render
from .models import Usuario, Promociones, Producto

# Create your views here.
def index(request):
   return render(request, 'index.html')


def usuario_lista(request):
    usuario = Usuario.objects.all()
    return render(request, 'formularios/usuario_lista.html',{"usuario_lista":usuario})
