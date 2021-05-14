from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Model com dados do corretor
class Corretor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='default.jpg', upload_to='corretor_pics')

    def __str__(self):
        return f'{self.user.username} Corretor'

# Model com dados da listagem do imóvel
class Imovel(models.Model):
    imovel = models.CharField(max_length=50, null=True)
    valor = models.DecimalField(max_digits=50, decimal_places=2)
    localizacao = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.imovel

# Model com dados da venda para realizar a simulação
class Venda(models.Model):
    PAGAMENTO_CHOICES = (
        ("À Vista", "À Vista"),
        ("180 Parcelas", "180 Parcelas"),
    )
    imovel = models.ForeignKey(Imovel, verbose_name=("Imóvel"), on_delete=models.CASCADE, null=True)
    corretor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Corretor"), on_delete=models.CASCADE)
    cliente = models.ForeignKey("cliente.Cliente", verbose_name=("Cliente"), on_delete=models.CASCADE)
    pagamento = models.CharField(max_length=30, choices=PAGAMENTO_CHOICES, null=True)

    def __str__(self):
        return f'{self.imovel.imovel} Venda'