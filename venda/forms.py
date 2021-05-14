from django import forms
from .models import Corretor, Venda
from django.contrib.auth.models import User

#Formulário de editar usuário
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

#Formulário de editar corretor
class CorretorUpdateForm(forms.ModelForm):

    class Meta:
        model = Corretor
        fields = ['imagem']

#Formulário de simulaçao da venda
class SimulacaoForm(forms.ModelForm):

    class Meta:
        model = Venda
        fields = '__all__'