from django.urls import path
from . import views
from .views import register, ImovelListView, VendaDetailView

# Criação de rotas com a chamada de suas respectivas views
urlpatterns = [
    path('registro/', register.as_view(), name='registro'),
    path('editar/', views.editCorretor, name='edit-corretor'),
    path('imovel/', ImovelListView.as_view(), name='imovel'),
    path('simulacao/<int:pk>', views.simulacao, name='simulacao'),
    path('venda/<int:pk>', VendaDetailView.as_view(), name='venda'),
]