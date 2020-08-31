from django.shortcuts import render
from .models import *
import socket
import requests


def get_ip_user():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
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

    def tres_dias():
        tres_dias = dict()
        tres_dias['dia'] = date['results']['forecast'][3]['weekday']
        tres_dias['maxima'] = date['results']['forecast'][3]['max']
        tres_dias['minima'] = date['results']['forecast'][3]['min']
        tres_dias['descricao'] = date['results']['forecast'][3]['description']

        return tres_dias

    def quatro_dias():
        quatro_dias = dict()
        quatro_dias['dia'] = date['results']['forecast'][4]['weekday']
        quatro_dias['maxima'] = date['results']['forecast'][4]['max']
        quatro_dias['minima'] = date['results']['forecast'][4]['min']
        quatro_dias['descricao'] = date['results']['forecast'][4]['description']

        return quatro_dias

    def cinco_dias():
        cinco_dias = dict()
        cinco_dias['dia'] = date['results']['forecast'][5]['weekday']
        cinco_dias['maxima'] = date['results']['forecast'][5]['max']
        cinco_dias['minima'] = date['results']['forecast'][5]['min']
        cinco_dias['descricao'] = date['results']['forecast'][5]['description']

        return cinco_dias

    def seis_dias():
        seis_dias = dict()
        seis_dias['dia'] = date['results']['forecast'][6]['weekday']
        seis_dias['maxima'] = date['results']['forecast'][6]['max']
        seis_dias['minima'] = date['results']['forecast'][6]['min']
        seis_dias['descricao'] = date['results']['forecast'][6]['description']

        return seis_dias

    def sete_dias():
        sete_dias = dict()
        sete_dias['dia'] = date['results']['forecast'][7]['weekday']
        sete_dias['maxima'] = date['results']['forecast'][7]['max']
        sete_dias['minima'] = date['results']['forecast'][7]['min']
        sete_dias['descricao'] = date['results']['forecast'][7]['description']

        return sete_dias

    def oito_dias():
        oito_dias = dict()
        oito_dias['dia'] = date['results']['forecast'][5]['weekday']
        oito_dias['maxima'] = date['results']['forecast'][5]['max']
        oito_dias['minima'] = date['results']['forecast'][5]['min']
        oito_dias['descricao'] = date['results']['forecast'][5]['description']

        return oito_dias

    hoje = hoje()
    amanha = amanha()
    dois = dois_dias()
    tres = tres_dias()
    quatro = quatro_dias()
    cinco = cinco_dias()
    seis = seis_dias()
    sete = sete_dias()
    oito = oito_dias()

    '''print(hoje)
    print(amanha)
    print(dois)
    print(tres)
    print(quatro)
    print(cinco)
    print(seis)
    print(sete)
    print(oito)
    lista = [amanha, dois, tres, quatro]
    for v in lista:
        for key, value in v.items():
            print(value)
        print()'''

    context = {'hoje': hoje,
               'amanha': amanha,
               'dois': dois,
               'tres': tres,
               'quatro': quatro,
               'cinco': cinco,
               'seis': seis,
               'sete': sete,
               'oito': oito}

    for key, value in context.items():
        for k, v in value.items():
            print(k, v)

    return render(request, 'clima.html', context)
