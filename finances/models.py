from django.db import models


class Real_Moeda(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=1)
    data = models.DateTimeField('Data', auto_now_add=True)

    def __str__(self):
        return self.name


class Dolar_Moeda(models.Model):
    name_dolar = models.CharField(max_length=50)
    buy_dolar = models.FloatField(null=True)
    sell_dolar = models.FloatField(null=True)
    variacao_dolar = models.FloatField(null=True)
    data_dolar = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_dolar


class Euro_Moeda(models.Model):
    name_euro = models.CharField(max_length=50)
    buy_euro = models.FloatField(null=True)
    sell_euro = models.FloatField(null=True)
    variacao_euro = models.FloatField(null=True)
    data_euro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_euro


class Libra_Esterlina_Moeda(models.Model):
    name_libra = models.CharField(verbose_name='Libra', max_length=50)
    buy_libra = models.FloatField(null=True)
    sell_libra = models.FloatField(null=True)
    variacao_libra = models.FloatField(null=True)
    data_libra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Libra'


class Peso_Argentino_Moeda(models.Model):
    name_peso = models.CharField(max_length=50)
    buy_peso = models.FloatField(null=True)
    sell_peso = models.FloatField(null=True)
    variacao_peso = models.FloatField(null=True)
    data_peso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_peso


class Preco_Moedas_Compra(models.Model):
    dolar = models.DecimalField(max_digits=8, decimal_places=2)
    euro = models.DecimalField(max_digits=8, decimal_places=2)
    libra = models.DecimalField(max_digits=8, decimal_places=2)
    peso = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateTimeField('Data', auto_now_add=True)


    def __str__(self):
        return f'Preço Moedas Compra'


class Preco_Moedas_Venda(models.Model):
    dolar = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    euro = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    libra = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    peso = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    data = models.DateTimeField('Data', auto_now_add=True)

    def __str__(self):
        return f'Preço Moedas Venda'

