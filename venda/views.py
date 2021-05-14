from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserUpdateForm, CorretorUpdateForm, SimulacaoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views import generic
from .models import Venda, Imovel

#View de registro do corretor
class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

#View de editar corretor
def editCorretor(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        c_form = CorretorUpdateForm(request.POST, request.FILES, instance=request.user.corretor)

        if u_form.is_valid() and c_form.is_valid():
            u_form.save()
            c_form.save()
            return redirect('cliente')
    else:
        u_form = UserUpdateForm(instance=request.user)
        c_form = CorretorUpdateForm(instance=request.user.corretor)

    context = {
        'u_form': u_form,
        'c_form': c_form
    }
    return render(request, 'venda/edit-corretor.html', context)

# View de Listagem dos Imóveis
class ImovelListView(ListView):
    model = Imovel
    template_name = "venda/imoveis.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imovel'] = Imovel.objects.all()
        return context

#View de detalhamento dos dados do imóvel e formulário para simulação
def simulacao(request, pk):
    imovel = Imovel.objects.get(pk=pk)

    if request.method == "POST":
        form = SimulacaoForm(request.POST)
        if form.is_valid():
            simulacao = form.save(commit=False)
            simulacao.corretor = request.user
            simulacao.save()
            return redirect('venda', pk=simulacao.id)
    else:
        form = SimulacaoForm()
        print(form.errors)
    
    context = {
        'imovel': imovel,
        'form': form
    }

    return render(request, 'venda/simulacao.html', context)
        
#View do resumo da simulação da venda
class VendaDetailView(DetailView):
    model = Venda
    template_name = "venda/resumo-venda.html"


