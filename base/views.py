from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
import math
from .forms import TanqueForm, TuberiaForm,Metodo2Form


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


def restart(request):
    print(request.META.get('HTTP_REFERER'))

    if request.GET.get('restart-si'):
        tuberias_pozo=[]
        tuberias_tp=[]
        tanques=[]
        return redirect('metodos') 
   
    ref = request.META.get('HTTP_REFERER')
    context={'ref':ref}
    return render(request, 'base/restart.html', context)

def metodos(request):
    global metodo
    metodo=0
    if request.GET.get('metodo-1'):
        metodo=1
        print(metodo)
        return redirect('form-tanques1')
    elif request.GET.get('metodo-2'):
        metodo=2;
        print(metodo)
        return redirect('form-metodo2')
    elif request.GET.get('metodo-3'):
        
        metodo=3;
        print(metodo)
        return redirect('')
        
    return render(request, 'base/metodos.html')

def seleccion_linear(request):
    
    return render(request, 'base/seleccion_linear.html')


def form_metodo2(request):
    form=Metodo2Form
    global tasa_de_bombeo
    global lectura_O3
    global vizcocidad_plastica
    global punto_cedente
    global densidad_lodo
    if request.method == 'POST':
        
        form = Metodo2Form(request.POST)
       
        if form.is_valid():
            tasa_de_bombeo=request.POST.get('tasa_bombeo')
            lectura_O3=request.POST.get('lectura_03')
            vizcocidad_plastica=request.POST.get('vizcocidad_plastica')
            punto_cedente=request.POST.get('punto_cedente')
            densidad_lodo=request.POST.get('densidad_lodo')
            return redirect('form-casing')
            
    
    context={'form':form}
    return render (request, 'base/form-metodo2.html',context)
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
            tanque1 = Tanque(float(weight), float(height), float(long), float(mud))
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
            tanque2 = Tanque(float(weight), float(height), float(long), float(mud))
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
            tanque3 = Tanque(float(weight), float(height), float(long), float(mud))
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
            casing = Tuberia(float(di), float(de), float(li), float(lf))
            casing.name = 'casing'
            tuberias_pozo.append(casing)
            
            

        return redirect('seleccion-linear')    
    
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
            linear1 = Tuberia(float(di), float(de), float(li), float(lf))
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
            linear2 = Tuberia(float(di), float(de), float(li), float(lf))
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
            open_hole = Tuberia(float(di), float(de), float(li), float(lf))
            open_hole.name = 'open_hole'
            tuberias_tp.append(open_hole)
            
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
            drillpipe = Tuberia(float(di), float(de), float(li), float(lf))
            drillpipe.name = 'drillpipe'
            tuberias_tp.append(drillpipe)
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
            bha = Tuberia(float(di), float(de), float(li), float(lf))
            bha.name = 'bha'
            tuberias_tp.append(bha)
            
            if metodo==1:
                return redirect('resultados-1')
            elif metodo==2:
                return redirect('resultados-2')
            elif metodo==3:
                return redirect('resultados-3')

    print(metodo)   
    context={'form':form}
    return render(request, 'base/form_bha.html', context)

#############################RESULTADOS##################################
def resultados1(request):
    
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
    volumen_desplazado = 0
    volumen_seccion_tp_total = 0
    volumen_pozo = 0
    volumen_anular = 0
    for tuberia in tuberias_tp:
        volumen_seccion_desplazado = ((((tuberia.de)**2)-((tuberia.di)**2))/1029.4) * (tuberia.lf - tuberia.li)
        volumen_desplazado += volumen_seccion_desplazado
        volumen_seccion_tp = (((tuberia.di)**2)/1029.4) * (tuberia.lf - tuberia.li)
        volumen_seccion_tp_total += volumen_seccion_tp

    for tuberia in tuberias_pozo:

        volumen_seccion_pozo = (((tuberia.di)**2)/1029.4) * tuberia.lt
        volumen_pozo += volumen_seccion_pozo

        if tuberia.name != 'open_hole':
            volumen_seccion_anular = ((((tuberia.di)**2)-((drillpipe.de)**2))/1029.4) * tuberia.lt
            volumen_anular += volumen_seccion_anular
        
        if tuberia.name == 'open_hole':
            
            if tuberia.li==bha.li:
                volumen_seccion_anular = ((((open_hole.di)**2)-((bha.de)**2))/1029.4) * (tuberia.lt)
                volumen_anular += volumen_seccion_anular
            elif tuberia.li<bha.li:
                volumen_seccion_anular = ((((open_hole.di)**2)-((drillpipe.de)**2))/1029.4) * (drillpipe.lf - open_hole.li)
                volumen_anular += volumen_seccion_anular
                volumen_seccion_anular = ((((open_hole.di)**2)-((bha.de)**2))/1029.4) * (open_hole.lf - bha.li)
                volumen_anular += volumen_seccion_anular
            elif tuberia.li>bha.li:
                print('ERROR ESTA FUERA DEL SCOPE DEL PROGRAMA')
                exit()

    volumen_total = volumen_anular + volumen_seccion_tp_total
    volumen_total_sistema = volumen_total + volumen_mud_bbl

    context={
        'capacidad_ss_bbl':capacidad_ss_bbl,
        'volumen_ss':volumen_ss,
        'volumen_mud':volumen_mud_bbl,
        'volumen_desplazado':volumen_desplazado,
        'volumen_seccion_tp_total':volumen_seccion_tp_total,
        'volumen_pozo':volumen_pozo,
        'volumen_anular':volumen_anular,
        'volumen_total_sistema':volumen_total_sistema
    }

    return render(request,'base/resultados-1.html', context)

def resultados2(request):

            #########CALCULO DE LAS DISTANCIAS DE CADA TRAMO
    m=0
    while m<=len(tuberias_pozo)-1:
        if m != len(tuberias_pozo)-1:
            tuberias_pozo[m].lt = tuberias_pozo[m+1].li - tuberias_pozo[m].li
            m+=1
        else:
            tuberias_pozo[m].lt = tuberias_pozo[m].lf - tuberias_pozo[m].li
            break

    return render(request,'base/resultados-2.html')