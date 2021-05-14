from django.contrib import admin
from .models import Corretor, Venda, Imovel

# Configurando models para aparecer no admin do django
admin.site.register(Corretor)
admin.site.register(Venda)
admin.site.register(Imovel)
