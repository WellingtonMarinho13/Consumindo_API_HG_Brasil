from django.forms import ModelForm
from .models import *


class Form_Real_Moeda(ModelForm):
    class Meta:
        model = Real_Moeda
        fields = ['name']


class Form_Dolar_Moeda(ModelForm):
    class Meta:
        model = Dolar_Moeda
        fields = ['name_dolar', 'buy_dolar', 'sell_dolar', 'variacao_dolar']


class Form_Euro_Moeda(ModelForm):
    class Meta:
        model = Euro_Moeda
        fields = ['name_euro', 'buy_euro', 'sell_euro', 'variacao_euro']


class Form_Libra_Moeda(ModelForm):
    class Meta:
        model = Libra_Esterlina_Moeda
        fields = ['name_libra', 'buy_libra', 'sell_libra', 'variacao_libra']


class Form_Peso_Moeda(ModelForm):
    class Meta:
        model = Peso_Argentino_Moeda
        fields = ['name_peso', 'buy_peso', 'sell_peso', 'variacao_peso']
