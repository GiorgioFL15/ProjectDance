from django.shortcuts import get_object_or_404, render
from .models import Noticia

def index(request):

    noticias = Noticia.objects.order_by('-date_receita').filter(publicada=True)

    dados = {
        'nome_das_noticias': noticias
    }
    return render(request, 'index.html', dados)

def noticias(request):
    return render(request,'noticias.html')


def noticia(request, id):
    noticia = get_object_or_404(Noticia, pk=id)

    noticia_a_exibir = {
        'noticia': noticia
    }
    return render(request,'noticias.html', noticia_a_exibir)
