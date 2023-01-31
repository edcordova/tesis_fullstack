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

class Metodo3FormJ(forms.Form):
    grado_azimud=  forms.FloatField(label = 'grado_azimud')
    distancia_azimud=  forms.FloatField(label = 'distancia_azimud')
    target_tvd= forms.FloatField(label = 'target_tvd')
    kop=forms.FloatField(label = 'kop')
    build_radius=forms.FloatField(label = 'build_radius')
    

class Metodo3FormS(forms.Form):
    grado_azimud=  forms.FloatField(label = 'grado_azimud')
    distancia_azimud=  forms.FloatField(label = 'distancia_azimud')
    target_tvd= forms.FloatField(label = 'target_tvd')
    kop=forms.FloatField(label = 'kop')
    build_radius=forms.FloatField(label = 'build_radius')
    drop_radius=forms.FloatField( label = 'drop_radius')
    

class Metodo3FormHorizontal(forms.Form):
    grado_azimud=  forms.FloatField(label = 'grado_azimud')
    distancia_azimud=  forms.FloatField(label = 'distancia_azimud')
    target_tvd= forms.FloatField(label = 'target_tvd')
    kop=forms.FloatField(label = 'kop')
    build_radius1=forms.FloatField(label = 'build_radius1')
    build_radius2=  forms.FloatField(label = 'build_radius2')
    
    