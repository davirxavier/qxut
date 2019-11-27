from django.db import models
from django.contrib.auth import get_user_model

class Perfil(models.Model):
	iduser = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name="perfil")
	nome = models.CharField(max_length = 200)
	sobrenome = models.CharField(max_length = 200)
	foto = models.FileField(upload_to='media/', null=True, blank=True)

class Amigo(models.Model):
	idperfil = models.ForeignKey(Perfil, related_name = 'amigo_idperfil', on_delete = models.CASCADE)
	amigo = models.ForeignKey(Perfil, related_name = 'amigo_perfil', on_delete = models.CASCADE)

class Postagem(models.Model):
	idperfil = models.ForeignKey(Perfil, on_delete = models.CASCADE, related_name = "postagens")		
	texto = models.CharField(max_length = 500)
	anexo = models.FileField(upload_to='media/', null=True, blank=True)
	data = models.DateTimeField()

class Comunidade(models.Model):
	nome = models.CharField(max_length = 300)
	descricao = models.CharField(max_length = 500)
	foto = models.FileField(upload_to='media/', null=True, blank=True)
	idadmin = models.ForeignKey(Perfil, related_name = "comunidades_admin", on_delete = models.CASCADE)

class Perfil_Comunidade(models.Model):
	idcomunidade = models.ForeignKey(Comunidade, on_delete = models.CASCADE, related_name = "comunidades")
	idperfil = models.ForeignKey(Perfil, on_delete = models.CASCADE)