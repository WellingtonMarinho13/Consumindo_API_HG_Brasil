from django.urls import path
from .views import *

urlpatterns = [
    path('', cidades, name='clima'),
    path('cidade/', cidade, name='cidade')
]
