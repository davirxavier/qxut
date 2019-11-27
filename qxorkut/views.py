from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm
from qxorkut.models import *
from django.contrib.auth import login, authenticate
import PIL

def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect("/qxut/login")

	perfil = request.user.perfil.first()

	postagens = perfil.postagens.all()

	context = {
		"perfil" : perfil, 
		"posts" : postagens,
		"username" : (perfil.nome + " " + perfil.sobrenome),
		"userimageurl" : perfil.foto.url,
	}

	return render(request, "main/index.html", context)


def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST, request.FILES)

		print(form.errors)
		if form.is_valid():
			user = form.save()

			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password1")

			perfil = Perfil()
			perfil.iduser = user
			perfil.nome = form.cleaned_data.get("firstname")
			perfil.sobrenome = form.cleaned_data.get("lastname")
			perfil.foto = form.cleaned_data.get("image")
			perfil.save()

			user.perfil.add(perfil)

			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect("/qxut/")

	else:
		form = RegisterForm()

	return render(request, "registration/register.html", {"form" : form})