from django import forms

class TanqueForm(forms.Form):
    weight = forms.FloatField(label = 'weight')
    height = forms.FloatField(label = 'weight')
    long = forms.FloatField(label = 'weight')
    mud = forms.FloatField(label = 'weight')