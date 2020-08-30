from django.shortcuts import render
from .models import CidadesID
import socket
import requests


def get_ip_user():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    ip = s.getsockname()[0]
    s.close()
    return ip


def cidade(request):
    cidade = requests.get(f'https://api.hgbrasil.com/weather?key=c95242d0&user_ip={ip}')
    cidade = cidade.json


""""
cidade = requests.get(f'https://api.hgbrasil.com/weather?key=c95242d0&user_ip={ip}')



date = cidade.json()


cidade = dict()
cidade['nome'] = date['results']['city']
cidade['temperatura'] = date['results']['temp']
cidade['maxima'] = date['results']['forecast'][0]['max']
cidade['minima'] = date['results']['forecast'][0]['min']
cidade['descricao'] = date['results']['description']

proximos_dias = dict()
proximos_dias['amanha']['dia'] = date['results']['forecast'][0]['weekday']
proximos_dias['amanha']['maxima'] = date['results']['forecast'][0]['max']
proximos_dias['amanha']['minima'] = date['results']['forecast'][0]['min']
proximos_dias['amanha']['descricao'] = date['results']['forecast'][0]['descricao']

print(cidade)
print()
print(proximos_dias)


print(time.strftime("%H:%M:%S %d-%m-%Y ", time.gmtime()))
"""

