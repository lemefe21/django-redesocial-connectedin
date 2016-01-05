# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.http import HttpResponse

# Create your views here.
# elaboramos uma resposta para o usuario sempre que ele acessar o navegador

#funções de view
@login_required # se não estiver logado será redirecionado para o login
def index(request):
	# funcao de view, chamada automaticamente
	# request - para interagir, pegar dados
	# (anteriormente) return HttpResponse('Bem vindo ao novo ConnectedIn!')

	#trabalhando com permissoes
	if request.user.has_perm('perfis.add_convite'):
		print 'Usuario tem a permissao dd_convite'
	else:
		print 'Usuario nao tem a permissao dd_convite'

	print request.user.email
	print request.user.username

	return render(request, 'index.html', { 'perfis' : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request) })	

@login_required
def exibir(request, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)

	perfil_logado = get_perfil_logado(request)
	ja_eh_contato = perfil in perfil_logado.contatos.all()

	print 'ID do perfil recebido: %s ' % (perfil_id)
	return render(request, 'perfil.html', { "perfil" : perfil, 'perfil_logado' : get_perfil_logado(request) , 'ja_eh_contato' : ja_eh_contato }) # chave/valor

#@permission_required('perfis.add_convite', raise_exception=True)
@login_required
def convidar(request, perfil_id):
	#pass #função para um método que não faz nada
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar) # metodo do models Perfil.convidar
	return redirect('index')

@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

@login_required
def get_perfil_logado(request):
	return request.user.perfil