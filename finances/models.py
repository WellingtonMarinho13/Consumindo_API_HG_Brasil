from django.db import models


class Base(models.Model):
    data = models.DateField('Data inicial', auto_now_add=True)
    atual = models.DateField('Atual', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Real_Moeda(Base):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=1)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Dolar_Moeda(Base):
    name_dolar = models.CharField(max_length=50)
    buy_dolar = models.FloatField(null=True)
    sell_dolar = models.FloatField(null=True)
    variacao_dolar = models.FloatField(null=True)
    data_dolar = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_dolar


class Euro_Moeda(Base):
    name_euro = models.CharField(max_length=50)
    buy_euro = models.FloatField(null=True)
    sell_euro = models.FloatField(null=True)
    variacao_euro = models.FloatField(null=True)
    data_euro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_euro


class Libra_Esterlina_Moeda(Base):
    name_libra = models.CharField(verbose_name='Libra', max_length=50)
    buy_libra = models.FloatField(null=True)
    sell_libra = models.FloatField(null=True)
    variacao_libra = models.FloatField(null=True)
    data_libra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Libra'


class Peso_Argentino_Moeda(Base):
    name_peso = models.CharField(max_length=50)
    buy_peso = models.FloatField(null=True)
    sell_peso = models.FloatField(null=True)
    variacao_peso = models.FloatField(null=True)
    data_peso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_peso
