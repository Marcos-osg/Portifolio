from os import name
from django.urls import path
from core import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contato',views.contato, name='contato'),
    path('galeria', views.galeria, name='galeria'),
    path('galeria/<int:pk>', views.foto, name='foto')
]