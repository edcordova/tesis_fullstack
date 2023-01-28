from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import math
from .forms import TanqueForm, TuberiaForm

class Tuberia:

    def __init__(self, di, de, li, lf):
        self.name = ''
        self.di = di
        self.de = de
        self.li = li
        self.lf = lf
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
    print(tuberias_pozo)
    return render(request, 'base/metodos.html')

def seleccion_tanques(request):
    
    return render(request, 'base/seleccion_tanques.html')

####################################################FORM TANQUES#########################
def form_tanques1(request):
    form = TanqueForm()
    
    if request.method == 'POST':
        
        form = TanqueForm(request.POST)
       
        if form.is_valid():
            weight=request.POST.get('weight')
            height=request.POST.get('height')
            long=request.POST.get('long')
            mud=request.POST.get('mud')
            global tanque1
            tanque1 = Tanque(int(weight), int(height), int(long), int(mud))
            tanques.append(tanque1)
            

        if 'button-continue' in request.POST:
           return redirect('form-tanques2')
        
        elif 'button-stop' in request.POST:
             return redirect('form-casing')
    
    
    context={'form':form}
    return render(request, 'base/form_tanques1.html', context)


def form_tanques2(request):
    form = TanqueForm()
    
    if request.method == 'POST':
        
        form = TanqueForm(request.POST)
       
        if form.is_valid():
            weight=request.POST.get('weight')
            height=request.POST.get('height')
            long=request.POST.get('long')
            mud=request.POST.get('mud')
            global tanque2
            tanque2 = Tanque(int(weight), int(height), int(long), int(mud))
            tanques.append(tanque2)
            

        if 'button-continue' in request.POST:
           return redirect('form-tanques3')
        
        elif 'button-stop' in request.POST:
             return redirect('form-casing')
    
    
    context={'form':form}
    return render(request, 'base/form_tanques2.html', context)

def form_tanques3(request):
    form = TanqueForm()
    
    if request.method == 'POST':
        
        form = TanqueForm(request.POST)
       
        if form.is_valid():
            weight=request.POST.get('weight')
            height=request.POST.get('height')
            long=request.POST.get('long')
            mud=request.POST.get('mud')
            global tanque3
            tanque3 = Tanque(int(weight), int(height), int(long), int(mud))
            tanques.append(tanque3)

        return redirect('form-casing')    
    
    context={'form':form}
    return render(request, 'base/form_tanques3.html', context)


#########################################################################################

def form_casing(request):
    form=TuberiaForm()

    if request.method == 'POST':
        
        form = TuberiaForm(request.POST)
       
        if form.is_valid():
            di=request.POST.get('di')
            de=request.POST.get('de')
            li=request.POST.get('li')
            lf=request.POST.get('lf')
            global casing
            casing = Tuberia(int(di), int(de), int(li), int(lf))
            casing.name = 'casing'
            tuberias_pozo.append(casing)
            

        return redirect('form-linear1')    

    context={'form':form}
    return render(request, 'base/form-casing.html', context)

def form_linear1(request):
    form=TuberiaForm()

    if request.method == 'POST':
        
        form = TuberiaForm(request.POST)
       
        if form.is_valid():
            di=request.POST.get('di')
            de=request.POST.get('de')
            li=request.POST.get('li')
            lf=request.POST.get('lf')
            global linear1
            linear1 = Tuberia(int(di), int(de), int(li), int(lf))
            linear1.name = 'linear1'
            tuberias_pozo.append(linear1)
            
            
        if 'button-continue' in request.POST:
            return redirect('form-linear2')
    
        elif 'button-stop' in request.POST:
            return redirect('form-openhole')

        
    context={'form':form}
    return render(request, 'base/form_linear1.html', context)

def form_linear2(request):
    form=TuberiaForm()

    if request.method == 'POST':
        
        form = TuberiaForm(request.POST)
       
        if form.is_valid():
            di=request.POST.get('di')
            de=request.POST.get('de')
            li=request.POST.get('li')
            lf=request.POST.get('lf')
            global linear2
            linear2 = Tuberia(int(di), int(de), int(li), int(lf))
            linear2.name = 'linear1'
            tuberias_pozo.append(linear2)
            
            return redirect('form-openhole')

        
    context={'form':form}
    return render(request, 'base/form_linear2.html', context)

def form_openhole(request):
    form=TuberiaForm()

    if request.method == 'POST':
        
        form = TuberiaForm(request.POST)
       
        if form.is_valid():
            di=request.POST.get('di')
            de=request.POST.get('de')
            li=request.POST.get('li')
            lf=request.POST.get('lf')
            global open_hole
            open_hole = Tuberia(int(di), int(de), int(li), int(lf))
            open_hole.name = 'open_hole'
            tuberias_pozo.append(open_hole)
            
            return redirect('form-drillpipe')

        
    context={'form':form}
    return render(request, 'base/form_openhole.html', context)

def form_drillpipe(request):
    form=TuberiaForm()

    if request.method == 'POST':
        
        form = TuberiaForm(request.POST)
       
        if form.is_valid():
            di=request.POST.get('di')
            de=request.POST.get('de')
            li=request.POST.get('li')
            lf=request.POST.get('lf')
            global drillpipe
            drillpipe = Tuberia(int(di), int(de), int(li), int(lf))
            drillpipe.name = 'drillpipe'
            tuberias_pozo.append(drillpipe)
            return redirect('form-bha')
            
            

        
    context={'form':form}
    return render(request, 'base/form_drillpipe.html', context)

def form_bha(request):
    form=TuberiaForm()

    if request.method == 'POST':
        
        form = TuberiaForm(request.POST)
       
        if form.is_valid():
            di=request.POST.get('di')
            de=request.POST.get('de')
            li=request.POST.get('li')
            lf=request.POST.get('lf')
            global bha
            bha = Tuberia(int(di), int(de), int(li), int(lf))
            bha.name = 'bha'
            tuberias_pozo.append(bha)
            for tuberia in tuberias_pozo:
                print(tuberia.name)
            return HttpResponse('We good')

        
    context={'form':form}
    return render(request, 'base/form_bha.html', context)


def resultados(request):
    if tanque1:
        capacidad_ss = 0
        volumen_ss = 0
        volumen_mud_bbl = 0
        capacidad_ss_bbl = 0

        for tanque in tanques:
            capacidad_tanque = tanque.weight * tanque.long * tanque.height
            capacidad_tanque_bbl = capacidad_tanque/5.615
            capacidad_ss += capacidad_tanque
            capacidad_ss_bbl += capacidad_tanque_bbl
            volumen_tanque = (tanque.weight * tanque.long)/5.615
            volumen_ss += volumen_tanque
            mud_level_ft = (volumen_tanque) * tanque.mud
            volumen_mud_bbl += mud_level_ft


    ########CALCULO DE LAS DISTANCIAS DE CADA TRAMO
    m=0
    while m<=len(tuberias_pozo)-1:
        if m != len(tuberias_pozo)-1:
            tuberias_pozo[m].lt = tuberias_pozo[m+1].li - tuberias_pozo[m].li
            m+=1
        else:
            tuberias_pozo[m].lt = tuberias_pozo[m].lf - tuberias_pozo[m].li
            break
    #####################################
    #CALCULO METODO 1
    volumen_pozo = 0
    volumen_anular = 0
    for tuberia in tuberias_pozo:
        if  tuberia.name != 'open_hole':
            volumen_seccion_pozo = (((tuberia.di)**2)/1029.4) * tuberia.lt
            volumen_pozo += volumen_seccion_pozo
            volumen_seccion_anular = ((((tuberia.di)**2)-((drillpipe.de)**2))/1029.4) * tuberia.lt
            volumen_anular += volumen_seccion_anular
        
        else:
            volumen_seccion_anular =((((open_hole.di)**2)-((drillpipe.de)**2))/1029.4) * (drillpipe.lf - open_hole.li)
            volumen_seccion_anular = ((((open_hole.di)**2)-((bha.de)**2))/1029.4) * (open_hole.lf - bha.li)
            volumen_anular += volumen_seccion_anular


    volumen_tp = 0
    volumen_desplazado = 0
    for tuberia in tuberias_tp:
        volumen_seccion_tp = (((tuberia.di)**2)/1029.4) * (tuberia.lf-tuberia.li)
        
        volumen_tp += volumen_seccion_tp

        volumen_seccion_desplazado = ((((tuberia.de)**2)-((tuberia.di)**2))/1029.4) * (tuberia.lf-tuberia.li)
        
        volumen_desplazado += volumen_seccion_desplazado


    volumen_total = volumen_anular + volumen_tp
    volumen_total_1 = volumen_pozo - volumen_desplazado
    print(volumen_total)




    return render(request,'restultados-1')