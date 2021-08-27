from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):

    opcao_status = [
        ('R', 'Rascunho'),
        ('P', 'Publicado')
    ]

    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    status = models.CharField(max_length=1, choices=opcao_status, blank=False, default="R")

    def __str__(self):
        return self.titulo