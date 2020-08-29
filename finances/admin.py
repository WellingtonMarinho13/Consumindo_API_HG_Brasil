from django.contrib import admin
from .models import *


@admin.register(Real_Moeda)
class Real_Moeda_Admin(admin.ModelAdmin):
    list_display = ('name', 'data')


@admin.register(Dolar_Moeda)
class Dolar_Moeda_Admin(admin.ModelAdmin):
    list_display = ('name_dolar', 'buy_dolar', 'sell_dolar', 'variacao_dolar', 'data_dolar')


@admin.register(Euro_Moeda)
class Euro_Moeda_Admin(admin.ModelAdmin):
    list_display = ('name_euro', 'buy_euro', 'sell_euro', 'variacao_euro', 'data_euro')


@admin.register(Libra_Esterlina_Moeda)
class Libra_Esterlina_Moeda_Admin(admin.ModelAdmin):
    list_display = ('get_name_libra', 'buy_libra', 'sell_libra', 'variacao_libra', 'data_libra')

    def get_name_libra(self, obj):
        return 'Libra Esterlina'

    get_name_libra.short_description = 'Libra Esterlina'



@admin.register(Peso_Argentino_Moeda)
class Peso_Argentino_Moeda_Admin(admin.ModelAdmin):
    list_display = ('name_peso', 'buy_peso', 'sell_peso', 'variacao_peso', 'data_peso')


@admin.register(Preco_Moedas_Compra)
class Preco_Moedas_Compra_Admin(admin.ModelAdmin):
    list_display = ('dolar', 'euro', 'libra', 'peso')


@admin.register(Preco_Moedas_Venda)
class Preco_Moedas_Venda_Admin(admin.ModelAdmin):
    list_display = ('dolar', 'euro', 'libra', 'peso')

