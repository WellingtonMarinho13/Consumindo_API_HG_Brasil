from django.urls import path
from .views import *

urlpatterns = [
    path('', cidades, name='cidades'),
    path('cidade', cidade, name='cidade')
]
