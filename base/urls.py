from django.urls import path

from . import views

urlpatterns = [
    path('metodos/', views.metodos, name='metodos'),
    path('seleccion-tanques/', views.seleccion_tanques, name='seleccion-tanques'),
    path('form-tanques1/', views.form_tanques1, name='form-tanques1'),
    path('form-tanques2/', views.form_tanques2, name='form-tanques2'),
    path('form-tanques3/', views.form_tanques3, name='form-tanques3'),
    path('form-casing/', views.form_casing, name='form-casing'),
    path('form-linear1/', views.form_linear1, name='form-linear1'),
    path('form-linear2/', views.form_linear2, name='form-linear2'),
    path('form-openhole/', views.form_openhole, name='form-openhole'),
    path('form-drillpipe/', views.form_drillpipe, name='form-drillpipe'),
    path('form-bha/', views.form_bha, name='form-bha'),
    path('resultados-1/', views.resultados, name='resultados'),
]