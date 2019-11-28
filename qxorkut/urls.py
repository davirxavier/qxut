from django.urls import include,path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name = 'register'),
    path('add_post/', views.atualizarPosts, name = "add_post"),
    path('', include('django.contrib.auth.urls'))
]