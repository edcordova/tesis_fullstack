from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
import math
from .forms import TanqueForm, TuberiaForm,Metodo2Form, Metodo3FormJ,Metodo3FormS,Metodo3FormHorizontal


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



# dicc={}
tuberias_pozo = []
tuberias_tp = []
tanques = []

def home(request):
    return render(request, 'base/home.html')

def restart(request):
    print(request.META.get('HTTP_REFERER'))

    if request.GET.get('restart-si'):
        tuberias_pozo=[]
        tuberias_tp=[]
        tanques=[]
        # dicc.clear()
        return redirect('home') 
   
    ref = request.META.get('HTTP_REFERER')
    context={'ref':ref}
    return render(request, 'base/restart.html', context)

def metodos(request):
    global metodo
    metodo=0
    if request.GET.get('metodo-1'):
        metodo=1
        return redirect('form-tanques1')
    elif request.GET.get('metodo-2'):
        metodo=2;
        return redirect('form-casing')
    elif request.GET.get('metodo-3'):
        metodo=3;
        return redirect('seleccion-metodo3')
        
    return render(request, 'base/metodos.html')

def seleccion_linear(request):
    
    return render(request, 'base/seleccion_linear.html')


def seleccion_metodo3(request):
    if request.GET.get('metodo-1'):
        return redirect('form-j')
    elif request.GET.get('metodo-2'):
        return redirect('form-s')
    elif request.GET.get('metodo-3'):
        return redirect('form-horizontal')

    return render(request , 'base/seleccion_metodo3.html')

def form_metodo2(request):
    form=Metodo2Form()
    global TASA_DE_BOMBEO
    global LECTURA_O3
    global VISCOCIDAD_PLASTICA
    global PUNTO_CEDENTE
    global DENSIDAD_LODO
   
    if request.method == 'POST':
        
        form = Metodo2Form(request.POST)
       
        if form.is_valid():
            
            TASA_DE_BOMBEO=form.cleaned_data.get('tasa_bombeo')
            LECTURA_O3=form.cleaned_data.get('lectura_03')
            VISCOCIDAD_PLASTICA=form.cleaned_data.get('vizcocidad_plastica')
            PUNTO_CEDENTE=form.cleaned_data.get('punto_cedente')
            DENSIDAD_LODO=form.cleaned_data.get('densidad_lodo')
            
            return redirect('resultados-2')
            
    
    context={'form':form}
    return render (request, 'base/form-metodo2.html',context)

####################################################FORM TANQUES#########################
def form_tanques1(request):
    form = TanqueForm()
    
    if request.method == 'POST':
        
        form = TanqueForm(request.POST)
       
        if form.is_valid():
            weight=form.cleaned_data.get('weight')
            height=form.cleaned_data.get('height')
            long=form.cleaned_data.get('long')
            mud=form.cleaned_data.get('mud')
            global tanque1
            tanque1 = Tanque(weight, height, long, mud)
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
            weight=form.cleaned_data.get('weight')
            height=form.cleaned_data.get('height')
            long=form.cleaned_data.get('long')
            mud=form.cleaned_data.get('mud')
            global tanque2
            tanque2 = Tanque(weight, height, long, mud)
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
            weight=form.cleaned_data.get('weight')
            height=form.cleaned_data.get('height')
            long=form.cleaned_data.get('long')
            mud=form.cleaned_data.get('mud')
            global tanque3
            tanque3 = Tanque(weight, height, long, mud)
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
            di=form.cleaned_data.get('di')
            de=form.cleaned_data.get('de')
            li=form.cleaned_data.get('li')
            lf=form.cleaned_data.get('lf')
            global casing
            casing = Tuberia(di, de, li, lf)
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
            di=form.cleaned_data.get('di')
            de=form.cleaned_data.get('de')
            li=form.cleaned_data.get('li')
            lf=form.cleaned_data.get('lf')
            global linear1
            linear1 = Tuberia(di, de, li, lf)
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
            di=form.cleaned_data.get('di')
            de=form.cleaned_data.get('de')
            li=form.cleaned_data.get('li')
            lf=form.cleaned_data.get('lf')
            global linear2
            linear2 = Tuberia(di, de, li, lf)
            linear2.name = 'linear2'
            tuberias_pozo.append(linear2)
            
            return redirect('form-openhole')

        
    context={'form':form}
    return render(request, 'base/form_linear2.html', context)

def form_openhole(request):
    form=TuberiaForm()

    if request.method == 'POST':
        
        form = TuberiaForm(request.POST)
       
        if form.is_valid():
            di=form.cleaned_data.get('di')
            de=form.cleaned_data.get('de')
            li=form.cleaned_data.get('li')
            lf=form.cleaned_data.get('lf')
            global open_hole
            open_hole = Tuberia(di, de, li, lf)
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
            di=form.cleaned_data.get('di')
            de=form.cleaned_data.get('de')
            li=form.cleaned_data.get('li')
            lf=form.cleaned_data.get('lf')
            global drillpipe
            drillpipe = Tuberia(di, de, li, lf)
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
            di=form.cleaned_data.get('di')
            de=form.cleaned_data.get('de')
            li=form.cleaned_data.get('li')
            lf=form.cleaned_data.get('lf')
            global bha
            bha = Tuberia(di, de, li, lf)
            bha.name = 'bha'
            tuberias_tp.append(bha)
            
            if metodo==1:
                return redirect('resultados-1')
            elif metodo==2:
                return redirect('form-metodo2')
            elif metodo==3:
                return redirect('resultados-3')

    print(metodo)   
    context={'form':form}
    return render(request, 'base/form_bha.html', context)

############################FORM METODO 3#############################
def form_j(request):
    form=Metodo3FormJ()
    global target_tvd
    global kop
    global build_radius
    global grado_azimud
    global distancia_azimud
    
    if request.method == 'POST':
        
        form = Metodo3FormJ(request.POST)
       
        if form.is_valid():
            target_tvd=form.cleaned_data.get('target_tvd')
            kop=form.cleaned_data.get('kop')
            build_radius=form.cleaned_data.get('build_radius')
            grado_azimud=form.cleaned_data.get('grado_azimud')
            distancia_azimud=form.cleaned_data.get('distancia_azimud')
            print(target_tvd, kop, build_radius)
            return redirect('form-casing')
            
    
    context={'form':form}
    return render (request, 'base/form-j.html', context)

def form_s(request):
    form=Metodo3FormS()
    global target_tvd
    global kop
    global build_radius
    global grado_azimud
    global distancia_azimud
    global drop_radius
    
    if request.method == 'POST':
        
        form = Metodo3FormS(request.POST)
       
        if form.is_valid():
            target_tvd=form.cleaned_data.get('target_tvd')
            kop=form.cleaned_data.get('kop')
            build_radius=form.cleaned_data.get('build_radius')
            drop_radius=form.cleaned_data.get('build_radius')
            grado_azimud=form.cleaned_data.get('grado_azimud')
            distancia_azimud=form.cleaned_data.get('distancia_azimud')
            print(target_tvd, kop, build_radius)
            return redirect('form-casing')
            
    
    context={'form':form}
    return render (request, 'base/form-s.html', context)

def form_horizontal(request):
    form=Metodo3FormHorizontal()
    global grado_azimud
    global distancia_azimud
    global target_tvd
    global kop
    global build_radius1
    global build_radius2
    
    if request.method == 'POST':
        
        form = Metodo3FormHorizontal(request.POST)
       
        if form.is_valid():
            target_tvd=form.cleaned_data.get('target_tvd')
            kop=form.cleaned_data.get('kop')
            build_radius1=form.cleaned_data.get('build_radius1')
            build_radius2=form.cleaned_data.get('build_radius2')
            grado_azimud=form.cleaned_data.get('grado_azimud')
            distancia_azimud=form.cleaned_data.get('distancia_azimud')
            print(target_tvd, kop, build_radius)
            return redirect('form-casing')
            
    
    context={'form':form}
    return render (request, 'base/form-horizontal.html', context)



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
    # TASA_DE_BOMBEO = 375
    # LECTURA_O3 = 5
    # VISCOCIDAD_PLASTICA = 32
    # PUNTO_CEDENTE = 19
    # DENSIDAD_LODO = 15.3


    # ############# DATOS TUBERIAS METODO 2
    # casing = Tuberia(12.515, 13.375, 0, 9360)
    # open_hole = Tuberia( 9.875, 0, 9360, 10500)
    # drillpipe = Tuberia(3.826, 4.5, 0, 10200)
    # bha = Tuberia(2.8125, 7.25, 10200, 10500)
    # casing.name = 'casing' 
    # open_hole.name = 'open_hole'
    # drillpipe.name = "drillpipe"
    # bha.name = "bha"
    # tuberias_pozo.append(casing)
    # tuberias_pozo.append(open_hole)
    # tuberias_tp.append(drillpipe)
    # tuberias_tp.append(bha)




    m=0
    while m<=len(tuberias_pozo)-1:
        if m != len(tuberias_pozo)-1:
            tuberias_pozo[m].lt = tuberias_pozo[m+1].li - tuberias_pozo[m].li
            m+=1
        else:
            tuberias_pozo[m].lt = tuberias_pozo[m].lf - tuberias_pozo[m].li
            break

    LECTURA_O600 = VISCOCIDAD_PLASTICA + VISCOCIDAD_PLASTICA + PUNTO_CEDENTE
    LECTURA_O300 = PUNTO_CEDENTE + VISCOCIDAD_PLASTICA
    CONSTANTE_NA = 0.5 * math.log (LECTURA_O300/LECTURA_O3, 10)
    CONSTANTE_KA = (5.11*LECTURA_O300)/((511**CONSTANTE_NA))
    CONSTANTE_NP = 3.32 * math.log10(LECTURA_O600/LECTURA_O300)
    CONSTANTE_KP = (5.11 * LECTURA_O600)/(1022**CONSTANTE_NP)
    REYNOLS_LAMINAR_A = 3470 - (1370*CONSTANTE_NA)
    REYNOLS_TURBULENTO_A = 4270 - (1370*CONSTANTE_NA)
    REYNOLS_LAMINAR_P = 3470 - (1370*CONSTANTE_NP)
    REYNOLS_TURBULENTO_P = 4270 - (1370*CONSTANTE_NP)

    ######## calculos de perdidas de presion dentro de la tuberia de perforacion
    PERDIDA_PRESION_P = 0
    for tuberia in tuberias_tp:
        
        VELOCIDAD_P = (0.408*TASA_DE_BOMBEO)/(tuberia.di**2)
        VISCOCIDAD_EFECTIVA_P = (100 * CONSTANTE_KP * (((96 * VELOCIDAD_P)/(tuberia.di))**(CONSTANTE_NP-1)))
        REYNOLS_P = (928 * VELOCIDAD_P * tuberia.di * DENSIDAD_LODO)/ (VISCOCIDAD_EFECTIVA_P * (((3*CONSTANTE_NP) +1)/(4*CONSTANTE_NP))**(CONSTANTE_NP))

        if  REYNOLS_P <= REYNOLS_LAMINAR_P :
            FANNY_P = 16 / REYNOLS_P
        elif REYNOLS_P >= REYNOLS_TURBULENTO_P :
            NUMERADOR = ((math.log10 (CONSTANTE_NP)+ 3.93) / 50)
            DENOMINADOR = ((1.75 - math.log10(CONSTANTE_NP))/7)
            FANNY_P = NUMERADOR / (REYNOLS_P**DENOMINADOR)
        else:
            NUMERADOR = ((math.log10 (CONSTANTE_NA)) / 50)
            DENOMINADOR = ((1.75 - math.log10(CONSTANTE_NA))/7)
            FANNY_P = ((REYNOLS_P - REYNOLS_LAMINAR_P)/800)*((NUMERADOR/(REYNOLS_LAMINAR_P**DENOMINADOR))-(16/REYNOLS_LAMINAR_P))
        PERDIDA_PRESION_P += (FANNY_P * (VELOCIDAD_P**2) * DENSIDAD_LODO * (tuberia.lf - tuberia.li))/(25.81 * tuberia.di)
        ##HUBO CAMBIO AQUI##
        

    # contador=1
    # contador_break=0
    dicc={}
    PERDIDA_PRESION=0

    for tuberia in tuberias_pozo:
        #########CASO BORDE OPEN HOLE
        if tuberia.name=='open_hole':

            if tuberia.li==bha.li:
                
                VELOCIDAD_CRITICA = ((REYNOLS_LAMINAR_A * 100 * CONSTANTE_KA * ((((2*CONSTANTE_NA)+1)/(3*CONSTANTE_NA))**CONSTANTE_NA))/(928 * DENSIDAD_LODO * (open_hole.di - bha.de)*((144/(open_hole.di - bha.de))**(1-CONSTANTE_NA))))**(1 / (2 - CONSTANTE_NA))
                TASA_BOMBEO_CRITICO = (2.45 * VELOCIDAD_CRITICA * ((open_hole.di**2) - (bha.de**2)))
                VELOCIDAD_ANULAR = (0.408*TASA_DE_BOMBEO)/((open_hole.di**2)-(bha.de**2))
                VISCOCIDAD_EFECTIVA_ANULAR = 100*CONSTANTE_KA*((144*VELOCIDAD_ANULAR)/(open_hole.di - bha.de))**(CONSTANTE_NA-1)
                REYNOLS = (928 * VELOCIDAD_ANULAR * (open_hole.di - bha.de) * DENSIDAD_LODO)/ (VISCOCIDAD_EFECTIVA_ANULAR * (((2*CONSTANTE_NA)+1/3*CONSTANTE_NA)**CONSTANTE_NA))

                if  REYNOLS <= REYNOLS_LAMINAR_A :
                    FANNY_ANULAR = 24 / REYNOLS
                elif REYNOLS >= REYNOLS_TURBULENTO_A :
                    NUMERADOR = ((math.log10 (CONSTANTE_NA)) / 50)
                    DENOMINADOR = ((1.75 - math.log10(CONSTANTE_NA))/7)
                    FANNY_ANULAR = NUMERADOR / (REYNOLS**DENOMINADOR)
                else:
                    NUMERADOR = ((math.log10 (CONSTANTE_NA)) / 50)
                    DENOMINADOR = ((1.75 - math.log10(CONSTANTE_NA))/7)
                    FANNY_ANULAR = ((REYNOLS - REYNOLS_LAMINAR_A)/800)*((NUMERADOR/(REYNOLS_LAMINAR_A**DENOMINADOR))-(24/REYNOLS_LAMINAR_A))

                PERDIDA_PRESION += (FANNY_ANULAR * (VELOCIDAD_ANULAR**2) * DENSIDAD_LODO * tuberia.lt) / (25.82 * (open_hole.di - bha.de))
                break           

            elif tuberia.li<bha.li:
                
                # contador_tp=contador
                for tp in tuberias_tp:
                    VELOCIDAD_CRITICA = ((REYNOLS_LAMINAR_A * 100 * CONSTANTE_KA * ((((2*CONSTANTE_NA)+1)/(3*CONSTANTE_NA))**CONSTANTE_NA))/(928 * DENSIDAD_LODO * (tuberia.di - tp.de)*((144/(tuberia.di - tp.de))**(1-CONSTANTE_NA))))**(1 / (2 - CONSTANTE_NA))
                    TASA_BOMBEO_CRITICO = (2.45 * VELOCIDAD_CRITICA * ((tuberia.di**2) - (tp.de**2)))
                    VELOCIDAD_ANULAR = (0.408*TASA_DE_BOMBEO)/((tuberia.di**2)-(tp.de**2))
                    VISCOCIDAD_EFECTIVA_ANULAR = 100*CONSTANTE_KA*((144*VELOCIDAD_ANULAR)/(tuberia.di - tp.de))**(CONSTANTE_NA-1)
                    REYNOLS = (928 * VELOCIDAD_ANULAR * (tuberia.di - tp.de) * DENSIDAD_LODO)/ (VISCOCIDAD_EFECTIVA_ANULAR * (((2*CONSTANTE_NA)+1/3*CONSTANTE_NA)**CONSTANTE_NA))

                    if  REYNOLS <= REYNOLS_LAMINAR_A :
                        FANNY_ANULAR = 24 / REYNOLS
                    elif REYNOLS >= REYNOLS_TURBULENTO_A :
                        NUMERADOR = ((math.log10 (CONSTANTE_NA)) / 50)
                        DENOMINADOR = ((1.75 - math.log10(CONSTANTE_NA))/7)
                        FANNY_ANULAR = NUMERADOR / (REYNOLS**DENOMINADOR)
                    else:
                        NUMERADOR = ((math.log10 (CONSTANTE_NA)) / 50)
                        DENOMINADOR = ((1.75 - math.log10(CONSTANTE_NA))/7)
                        FANNY_ANULAR = ((REYNOLS - REYNOLS_LAMINAR_A)/800)*((NUMERADOR/(REYNOLS_LAMINAR_A**DENOMINADOR))-(24/REYNOLS_LAMINAR_A))

                    if tp.name=='drillpipe':
                        PERDIDA_PRESION += (FANNY_ANULAR * (VELOCIDAD_ANULAR**2) * DENSIDAD_LODO * (drillpipe.lf - open_hole.li)) / (25.82 * (tuberia.di - tp.de))
                        
                    elif tp.name=='bha':
                        PERDIDA_PRESION += (FANNY_ANULAR * (VELOCIDAD_ANULAR**2) * DENSIDAD_LODO * (open_hole.lf - tp.li)) / (25.82 * (tuberia.di - tp.de))
                        
                    # dicc[f"seccion{contador_tp}"]=PERDIDA_PRESION

                    # contador_tp+=1
                    
                    # contador_break+=1
                    # if contador_break==2:
                    #     break               

            elif tuberia.li>bha.li:
                print('ERROR ESTA FUERA DEL SCOPE DEL PROGRAMA')
                exit()

        #########CALCULOS PARA CASING Y LINEARS EN CASO DE HABER        
        else:
            VELOCIDAD_CRITICA = ((REYNOLS_LAMINAR_A * 100 * CONSTANTE_KA * ((((2*CONSTANTE_NA)+1)/(3*CONSTANTE_NA))**CONSTANTE_NA))/(928 * DENSIDAD_LODO * (tuberia.di - drillpipe.de)*((144/(tuberia.di - drillpipe.de))**(1-CONSTANTE_NA))))**(1 / (2 - CONSTANTE_NA))
            TASA_BOMBEO_CRITICO = (2.45 * VELOCIDAD_CRITICA * ((tuberia.di**2) - (drillpipe.de**2)))
            VELOCIDAD_ANULAR = (0.408*TASA_DE_BOMBEO)/((tuberia.di**2)-(drillpipe.de**2))
            VISCOCIDAD_EFECTIVA_ANULAR = 100*CONSTANTE_KA*((144*VELOCIDAD_ANULAR)/(tuberia.di - drillpipe.de))**(CONSTANTE_NA-1)
            REYNOLS = (928 * VELOCIDAD_ANULAR * (tuberia.di - drillpipe.de) * DENSIDAD_LODO)/ (VISCOCIDAD_EFECTIVA_ANULAR * (((2*CONSTANTE_NA)+1/3*CONSTANTE_NA)**CONSTANTE_NA))

            if  REYNOLS <= REYNOLS_LAMINAR_A :
                FANNY_ANULAR = 24 / REYNOLS
            elif REYNOLS >= REYNOLS_TURBULENTO_A :
                NUMERADOR = ((math.log10 (CONSTANTE_NA)) / 50)
                DENOMINADOR = ((1.75 - math.log10(CONSTANTE_NA))/7)
                FANNY_ANULAR = NUMERADOR / (REYNOLS**DENOMINADOR)
            else:
                NUMERADOR = ((math.log10 (CONSTANTE_NA)) / 50)
                DENOMINADOR = ((1.75 - math.log10(CONSTANTE_NA))/7)
                FANNY_ANULAR = ((REYNOLS - REYNOLS_LAMINAR_A)/800)*((NUMERADOR/(REYNOLS_LAMINAR_A**DENOMINADOR))-(24/REYNOLS_LAMINAR_A))

            PERDIDA_PRESION += (FANNY_ANULAR * (VELOCIDAD_ANULAR**2) * DENSIDAD_LODO * tuberia.lt) / (25.82 * (tuberia.di - drillpipe.de))

            # dicc[f"seccion{contador}"]=PERDIDA_PRESION
            
        # contador+=1

             
    ECD = (PERDIDA_PRESION / (0.052*open_hole.lf))  + DENSIDAD_LODO
    PERDIDAS_TOTALES = PERDIDA_PRESION + PERDIDA_PRESION_P
    
    context={
        'PERDIDA_PRESION_P' : PERDIDA_PRESION_P,
        'PERDIDA_PRESION' : PERDIDA_PRESION,
        'PERDIDAS_TOTALES' : PERDIDAS_TOTALES,
        'ECD' : ECD
    }

    return render(request, 'base/resultados-2.html', context)

def resultados3j(request):
    return render(request,'base/')