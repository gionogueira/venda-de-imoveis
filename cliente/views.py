from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente

class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente/cliente.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente'] = Cliente.objects.all()
        return context

class ClienteCreateView(CreateView):
    model = Cliente
    fields = "__all__"
    template_name = "cliente/cliente_form.html"
    success_url = reverse_lazy('cliente')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = "__all__"
    template_name = "cliente/cliente_form.html"
    success_url = reverse_lazy('cliente')

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente')

