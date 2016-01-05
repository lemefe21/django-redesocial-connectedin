from django.conf.urls import patterns, include, url
from django.contrib import admin
from perfis import views

urlpatterns = patterns('',

	# 2 parametro da url: 'nome do modulo.nome do arquivo.funcao'
   
    url(r'^$', views.index, name='index'), #http://localhost:8000 >>>	
    #toda rota do django utiliza expressao regular

    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
    #http://localhost:8000/^perfis$
    #http://localhost:8000/^perfis/\d+$ - com um ou mais digitos numericos

    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),

    url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar'),

)
