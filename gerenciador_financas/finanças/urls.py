from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('transacoes/', views.transacoes_list, name='transacoes_list'),
    path('transacoes/add/', views.transacao_create, name='transacao_create'),
    path('transacoes/<int:pk>/delete/', views.transacao_delete, name='transacao_delete'),
]
