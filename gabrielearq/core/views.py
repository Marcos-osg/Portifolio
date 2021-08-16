from django.shortcuts import render
from core.models import Galeria, Categoria

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def galeria(request):
    categoria = request.GET.get('categoria')
    if categoria == None:
        fotos = Galeria.objects.all()
    else:
        fotos = Galeria.objects.filter(categoria__nome=categoria)

    categorias = Categoria.objects.all()

    context = {'categorias':categorias, 'fotos':fotos}
    return render(request, 'core/galeria.html', context)

def foto(request,pk):
    foto = Galeria.objects.get(id=pk)
    return render(request,'core/foto.html', {'foto':foto})

def contato(request):
    return render(request, 'core/contato.html')