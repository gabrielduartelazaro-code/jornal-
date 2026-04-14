from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artigos, name='lista'),
    path('artigo/<int:id>/', views.detalhe_artigo, name='detalhe'),
    path('artigo/<int:id>/comentarios/', views.comentarios, name='comentarios'),
]