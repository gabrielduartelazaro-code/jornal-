from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario

def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'lista.html', {'artigos': artigos})


def detalhe_artigo(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    return render(request, 'detalhe.html', {'artigo': artigo})


def comentarios(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    comentarios = Comentario.objects.filter(artigo=artigo)

    if request.method == 'POST':
        texto = request.POST.get('texto')
        if texto:
            Comentario.objects.create(artigo=artigo, texto=texto)
            return redirect('comentarios', id=id)

    return render(request, 'comentarios.html', {
        'artigo': artigo,
        'comentarios': comentarios
    })
    