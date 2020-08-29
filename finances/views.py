from django.shortcuts import render, redirect
import requests
from .forms import *


def index(request):
    recebe_dados_e_salvar(request)

    real = Real_Moeda.objects.last()
    euro = Euro_Moeda.objects.last()
    libra = Libra_Esterlina_Moeda.objects.last()
    peso = Peso_Argentino_Moeda.objects.last()
    dolar = Dolar_Moeda.objects.last()

    cambio = {'real': real,
              'euro': euro,
              'libra': libra,
              'peso': peso,
              'dolar': dolar}

    return render(request, 'index.html', cambio)


def recebe_dados_e_salvar(request):
    date_json = requests.get('https://api.hgbrasil.com/finance?key=66ad2e86')

    # REAL
    date_real = date_json.json()
    real = dict()
    real['name'] = date_real['results']['currencies']['source']
    create_date = Real_Moeda.objects.create(name=real['name'])
    create_date.save()


    # DOLAR
    date_dolar = date_json.json()
    dolar = dict()
    dolar['name'] = date_dolar['results']['currencies']['USD']['name']
    dolar['buy'] = date_dolar['results']['currencies']['USD']['buy']
    dolar['sell'] = date_dolar['results']['currencies']['USD']['sell']
    dolar['variacao'] = date_dolar['results']['currencies']['USD']['variation']
    create_date_dolar = Dolar_Moeda.objects.create(name_dolar=dolar['name'], buy_dolar=dolar['buy'],
                                             sell_dolar=dolar['sell'], variacao_dolar=dolar['variacao'])
    create_date_dolar.save()


    # EURO
    date_euro = date_json.json()
    date_euro = date_euro['results']['currencies']['EUR']
    euro = dict()
    euro['name'] = date_euro['name']
    euro['buy'] = date_euro['buy']
    euro['sell'] = date_euro['sell']
    euro['variacao'] = date_euro['variation']
    create_date_euro = Euro_Moeda.objects.create(name_euro=euro['name'], buy_euro=euro['buy'],
                                                sell_euro=euro['sell'], variacao_euro=euro['variacao'])
    create_date_euro.save()


    # LIBRA ESTERLINA
    date_libra = date_json.json()
    date_libra = date_libra['results']['currencies']['GBP']
    libra = dict()
    libra['name'] = date_libra['name']
    libra['buy'] = date_libra['buy']
    libra['sell'] = date_libra['sell']
    libra['variacao'] = date_libra['variation']
    create_date_libra = Libra_Esterlina_Moeda.objects.create(name_libra=libra['name'], buy_libra=libra['buy'],
                                                            sell_libra=libra['sell'], variacao_libra=libra['variacao'])
    create_date_libra.save()


    # PESO ARGENTINO
    date_peso = date_json.json()
    date_peso = date_peso['results']['currencies']['ARS']
    peso = dict()
    peso['name'] = date_peso['name']
    peso['buy'] = date_peso['buy']
    peso['sell'] = date_peso['sell']
    peso['variacao'] = date_peso['variation']
    create_date_peso = Peso_Argentino_Moeda.objects.create(name_peso=peso['name'], buy_peso=peso['buy'],
                                                           sell_peso=peso['sell'], variacao_peso=peso['variacao'])
    create_date_peso.save()
    return redirect('index')

