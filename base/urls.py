from django.urls import path

from . import views

urlpatterns = [
    path('metodos/', views.metodos, name='metodos'),
]