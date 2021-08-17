from core.models import Contato
from django.shortcuts import redirect, render
from core.models import Galeria, Categoria
from core.forms import FormContato
from django.core.validators import validate_email
from django.contrib import messages

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

def sobre(request):
    return render(request, 'core/sobre.html')

def foto(request,pk):
    foto = Galeria.objects.get(id=pk)
    return render(request,'core/foto.html', {'foto':foto})

def contato(request):
    if request.method != 'POST':
        return render(request, 'core/contato.html')
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    assunto = request.POST.get('assunto')
    mensagem = request.POST.get('mensagem')
    if not nome or not email or not assunto or not mensagem:
        messages.error(request, 'Nenhum campo pode estar em branco')
        return render(request, 'core/contato.html')
    try:
        validate_email(email)
    except:
        return render(request, 'core/contato.html')
    messages.success(request,'Sua mensagem foi enviada, em breve retornaremos o contato.')
    contato = Contato.objects.create(nome=nome, email=email, assunto=assunto, mensagem=mensagem)
    contato.save()
    return redirect('contato')