from django.shortcuts import render
from django.http import HttpResponse 
from django.template.loader import get_template 
from django.template import Context 
import datetime 
 

def horas_adelante(request, offset):  
    try: 
        offset = int(offset) 
    except ValueError: 
        raise Http404()  
    dt=datetime.datetime.now() +datetime.timedelta(hours=offset)        
    return render(request, 'ensayo.html', {'horas_adelante': offset ,'hora_siguiente': dt})