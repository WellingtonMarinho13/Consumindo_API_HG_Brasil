from django.db import models


class Clima_Now(models.Model):
    cidade = models.CharField('Cidade', max_length=100)
    data = models.DateTimeField('Agora', auto_now_add=True)
    temperatura = models.IntegerField('Temperatura')
    maxima = models.IntegerField('Máxima')
    minima = models.IntegerField('Mínima')
    descricao = models.CharField('Descrição', max_length=200, null=True)

    def __str__(self):
        return self.cidade

