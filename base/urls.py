from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('metodos/', views.metodos, name='metodos'),
    path('seleccion-linear/', views.seleccion_linear, name='seleccion-linear'),
    path('seleccion-metodo3/', views.seleccion_metodo3, name='seleccion-metodo3'),
    path('form-metodo2/', views.form_metodo2, name='form-metodo2'),
    path('form-tanques1/', views.form_tanques1, name='form-tanques1'),
    path('form-tanques2/', views.form_tanques2, name='form-tanques2'),
    path('form-tanques3/', views.form_tanques3, name='form-tanques3'),
    path('form-casing/', views.form_casing, name='form-casing'),
    path('form-linear1/', views.form_linear1, name='form-linear1'),
    path('form-linear2/', views.form_linear2, name='form-linear2'),
    path('form-openhole/', views.form_openhole, name='form-openhole'),
    path('form-drillpipe/', views.form_drillpipe, name='form-drillpipe'),
    path('form-bha/', views.form_bha, name='form-bha'),
    path('resultados-1/', views.resultados1, name='resultados-1'),
    path('resultados-2/', views.resultados2, name='resultados-2'),
    path('resultados-31/', views.resultados31, name='resultados-31'),
    path('resultados-32/', views.resultados32, name='resultados-32'),
    path('resultados-33/', views.resultados33, name='resultados-33'),
    path('restart/', views.restart, name='restart'),
    path('form-j/', views.form_j, name='form-j'),
    path('form-s/', views.form_s, name='form-s'),
    path('form-horizontal/', views.form_horizontal, name='form-horizontal'),
]