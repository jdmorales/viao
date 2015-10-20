from django.shortcuts import render_to_response,render, redirect
from django.http import HttpResponse 
from django.template.loader import get_template 
from django.template import Context, RequestContext
from django.contrib.auth.models import User
from viao.form import PersonaForm,CultivoForm
from viao.models import Persona,Jefe,Trabajador,Dueno,Cultivo
import datetime
from django.contrib.auth.decorators import login_required
from viao_projecy.settings import LOGIN_URL

@login_required(redirect_field_name=LOGIN_URL)
def horas_adelante(request):  
    dt=datetime.datetime.now()
    return render(request, 'Fecha_actual.html', {'horas_adelante': 2 ,'hora_siguiente': dt})
    
@login_required(redirect_field_name=LOGIN_URL)
def person(request):
    personas=Persona.objects.all()
    return render_to_response('list_Personas.html',{'personas':personas})
    
@login_required(redirect_field_name=LOGIN_URL)    
def fpersonas(request):
    if request.method == 'POST':
        if  request.user.is_superuser:
            tipoU='Dueno'
        else:
            p=Persona.objects.get(username=request.user.username)
            if p.tipo_usuario == 'Dueno':
                tipoU='Jefe'
            if p.tipo_usuario == 'Jefe':
                tipoU='Trabajador'	   
        form = PersonaForm(request.POST)

        if form.is_valid():

            nombre=form.cleaned_data['first_name']
            apellido=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            telefono=form.cleaned_data['telefono']
            direccion=form.cleaned_data['direccion']
            passw=form.cleaned_data['password']
            documento=form.cleaned_data['documento']
            tipoDoc=form.cleaned_data['tipo_documento']
            fechaN=form.cleaned_data['fechaNacimiento']
            username=documento

            u=Persona.objects.create_user(username=username,email=email,telefono=telefono,direccion=direccion,
                password=passw,documento=documento,tipo_documento=tipoDoc,tipo_usuario=tipoU,first_name=nombre,last_name=apellido,fechaNacimiento=fechaN)
            u.save()
            if tipoU=='Dueno':
                d=Dueno(documento_id=documento)
            if tipoU=='Jefe':
                d=Jefe(documento_id=documento,dueno_id=p.documento)
            if tipoU=='Trabajador':
                d=Trabajador(documento_id=documento,jefe_id=p.documento)
            d.save()

            #form.save()
            return redirect("crear_personas")
    else:
        form = PersonaForm()
    return render_to_response('Form_usuario.html',{'form':form },context_instance=RequestContext(request))

@login_required(redirect_field_name=LOGIN_URL)    
def fcultivo(request):
    if request.method == 'POST':
        form = CultivoForm(request.POST)
        if form.is_valid():
            area=form.cleaned_data['area']
            tipoMedida='M2'
            jefe='2'
            dueno='1'
            fechaR=datetime.datetime.now()

            u=Cultivo(area=area,tipoMedida=tipoMedida,jefe_id=jefe,dueno_id=dueno,fechaRegsitro=fechaR)
            u.save()
            #form.save()
            return redirect("crear_cultivo")
    else:
        form = CultivoForm()
    return render_to_response('Form_Cultivo.html',{'form':form },context_instance=RequestContext(request))
    
@login_required(redirect_field_name=LOGIN_URL)
def inicio(request):
    persona=Persona.objects.get(username=request.user.username)
    return render_to_response('inicio.html',{'persona':persona})
