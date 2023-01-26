from django.shortcuts import render
from django.http import HttpResponse

def metodos(request):
    
    return render(request, 'base/metodos.html')