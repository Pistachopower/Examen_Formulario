from django.urls import path
from .import views


urlpatterns = [
   path('', views.index, name='index'),
   path('usuario/lista',views.usuario_lista,name='usuario_lista'), 
   
]
