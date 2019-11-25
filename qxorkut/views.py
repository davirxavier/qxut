from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm
from qxorkut.models import *

def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect("/qxut/login")

	perfil = request.user.perfil.first()

	postagens = perfil.postagens.all()

	return render(request, "main/index.html", {"perfil" : perfil, "posts" : postagens})


def register(request):
	form = RegisterForm()

	return render(request, "registration/register.html", {"form" : form})