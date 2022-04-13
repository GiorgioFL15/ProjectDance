from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/<int:id>', views.noticia, name='noticia'),
    path('noticias/', views.noticias, name='noticias')
]
