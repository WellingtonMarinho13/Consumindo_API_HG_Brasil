from django.shortcuts import render
from .models import *
import socket
import requests


def get_ip_user():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    ip = s.getsockname()[0]
    s.close()
    return ip


def previsao_clima(request):
    get_ip_user()
    ip = get_ip_user()

    cidade = requests.get(f'https://api.hgbrasil.com/weather?key=c95242d0&user_ip={ip}')

    date = cidade.json()

    def hoje():
        hoje = dict()
        hoje['nome'] = date['results']['city']
        hoje['temperatura'] = date['results']['temp']
        hoje['maxima'] = date['results']['forecast'][0]['max']
        hoje['minima'] = date['results']['forecast'][0]['min']
        hoje['descricao'] = date['results']['description']
        create = Clima_Now.objects.create(cidade=hoje['nome'],
                                          temperatura=hoje['temperatura'],
                                          maxima=hoje['maxima'],
                                          minima=hoje['minima'],
                                          descricao=hoje['descricao'])
        create.save()
        create = None
        return hoje

    def amanha():
        amanha = dict()
        amanha['dia'] = date['results']['forecast'][1]['weekday']
        amanha['maxima'] = date['results']['forecast'][1]['max']
        amanha['minima'] = date['results']['forecast'][1]['min']
        amanha['descricao'] = date['results']['forecast'][1]['description']

        return amanha

    def dois_dias():
        dois_dias = dict()
        dois_dias['dia'] = date['results']['forecast'][2]['weekday']
        dois_dias['maxima'] = date['results']['forecast'][2]['max']
        dois_dias['minima'] = date['results']['forecast'][2]['min']
        dois_dias['descricao'] = date['results']['forecast'][2]['description']

        return dois_dias

    hoje = hoje()
    amanha = amanha()
    dois = dois_dias()

    print(hoje)
    print(amanha)
    print(dois)

    context = {'hoje': hoje,
               'amanha': amanha,
               'dois': dois}
    return render(request, 'clima.html', context)
