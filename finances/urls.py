from django.urls import path
from .views import *

urlpatterns = [
    path('', atualiza, name='atualiza'),
    path('index/', Index.as_view(), name='index'),

]
