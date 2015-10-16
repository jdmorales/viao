from django.shortcuts import render_to_response,render, redirect,get_object_or_404
from django.http import HttpResponse 
from django.template.loader import get_template 
from django.template import Context, RequestContext
from django.contrib.auth.models import User
from viao.form import PersonaForm
from viao.models import Persona
import datetime
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def horas_adelante(request):  
    dt=datetime.datetime.now()
    return render(request, 'Fecha_actual.html', {'horas_adelante': 2 ,'hora_siguiente': dt})
    
@login_required(redirect_field_name='login')
def person(request):
    personas=Persona.objects.all()
    return render_to_response('list_Personas.html',{'personas':personas})

@login_required(redirect_field_name='login')
def fpersonas(request):
    if request.method == 'POST':	
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("personas")
    else:
        form = PersonaForm()
	return render_to_response('Form_persona.html',{'form':form },context_instance=RequestContext(request))
