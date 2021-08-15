from django.db import models

# Create your models here.

class Galeria(models.Model):
    imagem = models.ImageField(upload_to = 'media/%Y/%m/%d' ,verbose_name='Imagem')
    descricao = models.TextField(verbose_name='Descrição')
    categoria = models.TextField(verbose_name='Categoria')

    def __str__(self):
        return self.descricao


class Contato(models.Model):
    nome = models.TextField(verbose_name='Nome')
    email = models.TextField(verbose_name='E-mail')
    assunto = models.TextField(verbose_name='Assunto')
    mensagem = models.TextField(verbose_name='Mensagem')

    def __str__(self):
        return self.nome 