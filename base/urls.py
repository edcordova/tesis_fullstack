from django.urls import path

from . import views

urlpatterns = [
    path('metodos/', views.metodos, name='metodos'),
    path('seleccion-tanques/', views.seleccion_tanques, name='seleccion-tanques'),
    path('form-tanques1/', views.form_tanques1, name='form-tanques1'),
]