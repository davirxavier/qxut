from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm
from qxorkut.models import *
from django.contrib.auth import login, authenticate
import PIL
from datetime import datetime
import pytz
from .forms import PostarForm

def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

def getTimedeltaString(t):
	strdelta = strfdelta(t, "{days}") + " dias"
	if strdelta == "0 dias":
		strdelta = strfdelta(t, "{hours}") + " horas"
		if strdelta == "0 horas":
			strdelta = strfdelta(t, "{minutes}") + " minutos"
			if strdelta == "0 minutos":
				strdelta = strfdelta(t, "{seconds}") + " segundos"
				return strdelta
			return strdelta
		return strdelta
	return strdelta

def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect("/qxut/login")

	perfil = request.user.perfil.first()
	postagens = perfil.postagens.all()
	comunidades = perfil.comunidades.all()
	amigos = perfil.amigos.all()

	for postagem in postagens:
		data = postagem.data.replace(tzinfo=pytz.utc)
		now = datetime.now(pytz.utc)
		diff = now - data
		postagem.ago = getTimedeltaString(diff)

	form = PostarForm()

	context = {
		"perfil" : perfil, 
		"posts" : postagens,
		"username" : (perfil.nome + " " + perfil.sobrenome),
		"userimage" : perfil.foto,
		"comunidades" : comunidades,
		"amigos" : amigos,
		"form" : form
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