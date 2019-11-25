from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	firstname = forms.CharField(max_length = 200, min_length = 1)
	lastname = forms.CharField(max_length = 200, min_length = 1)
	email = forms.EmailField()
	image = forms.ImageField()
