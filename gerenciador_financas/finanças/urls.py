from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('transacoes/', views.transacoes_list, name='transacoes_list'),
    path('transacoes/add/', views.transacao_create, name='transacao_create'),
    path('transacoes/<int:pk>/delete/', views.transacao_delete, name='transacao_delete'),
    path('cotacao/', views.cotacao_view, name='cotacao'),
    path('adicionar_ticker/', views.adicionar_ticker, name='adicionar_ticker'),
    path('excluir_ticker/<str:ticker_nome>/', views.excluir_ticker, name='excluir_ticker'),
    path('upload_recibo/', views.upload_recibo, name='upload_recibo'),
]
