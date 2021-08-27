from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo