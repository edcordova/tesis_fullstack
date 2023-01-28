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

   