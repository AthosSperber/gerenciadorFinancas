from django.urls import path
from . import views

urlpatterns = [
    path('transacoes/', views.transacoes_list, name='transacoes_list'),
    path('transacoes/add/', views.transacao_create, name='transacao_create'),
]
