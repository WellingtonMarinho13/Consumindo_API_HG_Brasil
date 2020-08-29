from django.db import models


class Base(models.Model):
    data = models.DateTimeField('Data inicial', auto_now_add=True)
    atual = models.DateField('Atual', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class CidadesID(Base):
    nome_cidade = models.CharField('Nome', max_length=100)
    woe_id = models.IntegerField('Código da Cidade')

    def __str__(self):
        return self.nome_cidade

