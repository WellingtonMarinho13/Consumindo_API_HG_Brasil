from django.shortcuts import render, redirect
import requests
from .forms import *
from django.views.generic import ListView


class Index(ListView):
    model = Preco_Moedas_Compra
    template_name = 'index.html'
    paginate_by = 10
    context_object_name = 'moedas'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').all()

        return qs


def atualiza(request):
    recebe_dados_e_salvar(request)
    return redirect('index')


def recebe_dados_e_salvar(request):
    date_json = requests.get('https://api.hgbrasil.com/finance?key=66ad2e86')

    # REAL
    def real():
        date_real = date_json.json()
        real = dict()
        real['name'] = date_real['results']['currencies']['source']
        create_date = Real_Moeda.objects.create(name=real['name'])
        create_date.save()

    # DOLAR
    def dolar():
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
    def euro():
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
    def libra():
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
    def peso():
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

    # Preco todas as moedas compra, venda e data
    def preco_moedas_compra():
        moeda = date_json.json()

        dolar_buy = moeda['results']['currencies']['USD']['buy']
        euro_buy = moeda['results']['currencies']['EUR']['buy']
        libra_buy = moeda['results']['currencies']['GBP']['buy']
        peso_buy = moeda['results']['currencies']['ARS']['buy']
        create_Preco_Moedas_Compra = Preco_Moedas_Compra.objects.create(dolar=dolar_buy,
                                                          euro=euro_buy,
                                                          libra=libra_buy,
                                                          peso=peso_buy)
        create_Preco_Moedas_Compra.save()

    def preco_moedas_venda():
        moeda = date_json.json()

        dolar_sell = moeda['results']['currencies']['USD']['sell']
        euro_sell = moeda['results']['currencies']['EUR']['sell']
        libra_sell = moeda['results']['currencies']['GBP']['sell']
        peso_sell = moeda['results']['currencies']['ARS']['sell']
        create_Preco_Moedas_Venda = Preco_Moedas_Venda.objects.create(dolar=dolar_sell,
                                                                 euro=euro_sell,
                                                                 libra=libra_sell,
                                                                 peso=peso_sell)
        create_Preco_Moedas_Venda.save()

    real()
    dolar()
    euro()
    libra()
    peso()
    preco_moedas_compra()
    preco_moedas_venda()

    return redirect('index')
