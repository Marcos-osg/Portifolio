from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.TextField(max_length=100, null= False, blank=False ,verbose_name='Categoria')

    def __str__(self):
        return self.nome


class Galeria(models.Model):
    imagem = models.ImageField(upload_to = 'media/%Y/%m/%d' ,verbose_name='Imagem')
    descricao = models.TextField(verbose_name='Descrição')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.descricao


class Contato(models.Model):
    nome = models.TextField(verbose_name='Nome')
    email = models.TextField(verbose_name='E-mail')
    assunto = models.TextField(verbose_name='Assunto')
    mensagem = models.TextField(verbose_name='Mensagem')

    def __str__(self):
        return self.nome 