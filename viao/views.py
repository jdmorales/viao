from django.shortcuts import render_to_response,render,redirect
from django.http import JsonResponse, Http404
from django.template.loader import get_template 
from django.template import Context, RequestContext
from django.contrib.auth.models import User
from viao.form import PersonaForm,CultivoForm
from viao.models import Persona,Dueno,Jefe,Trabajador,Cultivo,Lote
import datetime
from django.contrib.auth.decorators import login_required
from viao_projecy.settings import LOGIN_URL

@login_required(redirect_field_name=LOGIN_URL)
def horas_adelante(request):  
    dt=datetime.datetime.now()
    return render(request, 'Fecha_actual.html', {'horas_adelante': 2 ,'hora_siguiente': dt})
    
@login_required(redirect_field_name=LOGIN_URL)
def person(request):
    if not request.user.is_superuser:
        user=Persona.objects.get(username=request.user.username)
        users=Persona.objects.all()
        return render_to_response('list_Personas.html',{'user':user,'users':users})
    else:
        users=Persona.objects.all()
        return render_to_response('list_Personas.html',{'user':request.user,'users':users})
    
@login_required(redirect_field_name=LOGIN_URL)
def fpersonas(request):
    if  request.user.is_superuser:
        tipoU='Dueno'
        p=request.user
    else:
        p=Persona.objects.get(username=request.user.username)
        if p.tipo_usuario == 'Dueno':
            tipoU='Jefe'
        if p.tipo_usuario == 'Jefe':
            tipoU='Trabajador'
    if request.is_ajax and request.method == 'POST':
        errores=''
        exito=False	   
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
            exito=True
        else:
            errores = form.errors    
        response = {'exito':exito,'errores':errores}
        return JsonResponse(response)
    else:
        form = PersonaForm()
    return render_to_response('Form_usuario.html',{'user':p,'tipo_usuario':tipoU,'form':form },context_instance=RequestContext(request))

@login_required(redirect_field_name=LOGIN_URL)    
def fcultivo(request):
    user=Persona.objects.get(username=request.user.username)
    jefes=Jefe.objects.all().filter(dueno_id=user.documento)
    if request.method == 'POST':
        form = CultivoForm(request.POST)
        if form.is_valid():
            temp=form.save(commit=False)
            temp.tipoMedida='M2'
            temp.fechaRegsitro=datetime.datetime.now()
            temp.dueno_id=user.documento
            temp.save()
            return redirect("crear_cultivo")
    else:
         form = CultivoForm()
    return render_to_response('Form_Cultivo.html',{'user':user,'jefes':jefes,'form':form },context_instance=RequestContext(request))


@login_required(redirect_field_name=LOGIN_URL)
def inicio(request):
    if not request.user.is_superuser:
        user=Persona.objects.get(username=request.user.username)
        return render_to_response('inicio.html',{'user':user})
    else:
        return render_to_response('inicio.html',{'user':request.user})

@login_required(redirect_field_name=LOGIN_URL)
def inf_user(request):
    if not request.user.is_superuser:
        user=Persona.objects.get(username=request.user.username)
        
        if user.tipo_usuario == 'Dueno':
            asignaciones=Cultivo.objects.all().filter(dueno_id=user.documento)
        if user.tipo_usuario == 'Jefe':
            asignaciones=Trabajador.objects.all()._next_is_sticky().filter(jefe__documento=user.documento)
        if user.tipo_usuario == 'Trabajador':
            asignaciones=Lote.objects.all().filter(trabajador_id=user.documento)
        return render_to_response('inf_usuario.html',{'user':user,'asignaciones':asignaciones})
    else:
        asignaciones=Persona.objects.all().filter(tipo_usuario='Dueno')
        return render_to_response('inf_usuario.html',{'user':request.user,'asignaciones':asignaciones})


