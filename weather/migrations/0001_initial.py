# Generated by Django 2.2.3 on 2020-08-29 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CidadesID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data inicial')),
                ('atual', models.DateField(auto_now=True, verbose_name='Atual')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome_cidade', models.CharField(max_length=100, verbose_name='Nome')),
                ('woe_id', models.IntegerField(verbose_name='Código da Cidade')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
