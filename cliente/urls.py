from django.urls import path
from . import views
from cliente.views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

# Criação de rotas com a chamada de suas respectivas views  
urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente'),
    path('cadastro/', ClienteCreateView.as_view(), name='criar-cliente'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='editar-cliente'),
    path('deletar/<int:pk>/', ClienteDeleteView.as_view(), name='deletar-cliente'),
]