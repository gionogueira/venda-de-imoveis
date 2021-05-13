from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=60, null = True)
    cpf = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=30)
    imagem = models.ImageField(default='default.jpg', upload_to='client_pics')

    def __str__(self):
        return self.nome
    