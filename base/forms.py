from django import forms

class TanqueForm(forms.Form):
    weight = forms.FloatField(label = 'weight')
    height = forms.FloatField(label = 'height')
    long = forms.FloatField(label = 'long')
    mud = forms.FloatField(label = 'mud')

class TuberiaForm(forms.Form):
    di = forms.FloatField(label = 'di')
    de = forms.FloatField(label = 'de')
    li = forms.FloatField(label = 'li')
    lf = forms.FloatField(label = 'lf')

class Metodo2Form(forms.Form):
    tasa_bombeo= forms.FloatField(label = 'tasa_bombeo')
    lectura_03=forms.FloatField(label = 'lectura_03')
    vizcocidad_plastica=forms.FloatField(label = 'vizcocidad_plastica')
    punto_cedente=forms.FloatField(label = 'punto_cedente')
    densidad_lodo=  forms.FloatField(label = 'densidad_lodo')

    