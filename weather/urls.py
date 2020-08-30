from django.urls import path
from .views import *

urlpatterns = [
    path('', previsao_clima, name='clima'),
]
