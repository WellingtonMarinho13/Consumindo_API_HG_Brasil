from django.shortcuts import render
from .models import CidadesID


def cidades(request):
    cidades = CidadesID.objects.all()

    return render(request, 'cidades.html', {'cids': cidades})


def cidade(request):
    cidades = CidadesID.objects.all()

    return render(request, 'cidade.html', {'cids': cidades})
