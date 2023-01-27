from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import math
from .forms import TanqueForm

class Tuberia:

    def __init__(self, di, de, li, lf, peso):
        self.name = ''
        self.di = di
        self.de = de
        self.li = li
        self.lf = lf
        self.peso = peso
        self.lt = 0

class Tanque:
    def __init__(self, weight, height, long, mud):
        self.weight = weight
        self.height = height
        self.long = long
        self.mud = mud

dicc={}
tuberias_pozo = []
tuberias_tp = []
tanques = []

def metodos(request):
    
    return render(request, 'base/metodos.html')

def seleccion_tanques(request):
    
    return render(request, 'base/seleccion_tanques.html')

def form_tanques1(request):
    form = TanqueForm()

     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        
        form = TanqueForm(request.POST)
       
        if form.is_valid():
            weight=request.POST.get('weight')
            dicc['weight']=weight
            print(dicc)
            return HttpResponseRedirect('/thanks/')
    
    
    context={'form':form}
    return render(request, 'base/form_tanques1.html', context)
