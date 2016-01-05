from django.shortcuts import render, redirect
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from perfis.models import Perfil

# class based view
class RegistrarUsuarioView(View):

	template_name = 'registrar.html'

	def get(self, request): #exibir o formulario para o usuario
		return render(request, self.template_name)

	def post(self, request): #lidar com os dados do formulario

		form = RegistrarUsuarioForm(request.POST)

		if form.is_valid():
			dados_form = form.data

			#se os dados do formulario estiverem corretos
			usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])

			#passa o usuario criado para o Perfil
			perfil = Perfil(nome=dados_form['nome'], 
							email=dados_form['email'], 
							telefone=dados_form['telefone'],
							nome_empresa=dados_form['nome_empresa'],
							usuario=usuario) # OneToOne

			perfil.save()
			return redirect('index')

		#se nao for valido
		#passo o form para mostrar o formulario preenchido
		return render(request, self.template_name, {'form' : form})
