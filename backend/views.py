from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, RequestContext, render
from django.http import JsonResponse

from django.template import Context, RequestContext
from django.contrib.auth.models import User
from backend.form import PersonaForm, CultivoForm, EditarPersonaForm, EditarCultivoForm
from backend.models import Persona, Dueno, Jefe, Trabajador, Cultivo, Lote
import datetime
from django.contrib.auth.decorators import login_required
from viao_projecy.settings import LOGIN_URL
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
import json
import yaml
import hashlib

class log():
    @staticmethod
    def log_in(request, *args, **kwargs):
        print(request.POST)
        response = {'msn': 3, 'exito': 3, 'errores': 1}
        return JsonResponse(response)

    @staticmethod
    def log_out(request, *args, **kwargs):
        logout(request)


@login_required(redirect_field_name=LOGIN_URL)
def horas_adelante(request):
    dt = datetime.datetime.now()
    return render(request, 'Fecha_actual.html', {'horas_adelante': 2, 'hora_siguiente': dt})


@login_required(redirect_field_name=LOGIN_URL)
def listar(request):
    if not request.user.is_superuser:
        user = Persona.objects.get(username=request.user.username)
        if user.tipo_usuario == 'Dueno':
            users = Jefe.objects.all().filter(Q(dueno_id=user.documento) & Q(activo=True));
        if user.tipo_usuario == 'Jefe':
            users = Trabajador.objects.all().filter(Q(jefe_id=user.documento) & Q(activo=True));
        return render_to_response('list_Personas.html', {'user': user, 'users': users})
    else:
        users = Dueno.objects.all().filter(activo=True)
        return render_to_response('list_Personas.html', {'user': request.user, 'users': users})


@login_required(redirect_field_name=LOGIN_URL)
def crear_usuario(request):
    msn = False
    if request.user.is_superuser:
        tipoU = 'Dueno'
        p = request.user
    else:
        p = Persona.objects.get(username=request.user.username)
        if p.tipo_usuario == 'Dueno':
            tipoU = 'Jefe'
        if p.tipo_usuario == 'Jefe':
            tipoU = 'Trabajador'
    if request.is_ajax and request.method == 'POST':
        errores = ''
        exito = False
        form = PersonaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['first_name']
            apellido = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            direccion = form.cleaned_data['direccion']
            passw = form.cleaned_data['password']
            documento = form.cleaned_data['documento']
            tipoDoc = form.cleaned_data['tipo_documento']
            fechaN = form.cleaned_data['fechaNacimiento']
            username = documento
            u = Persona.objects.create_user(username=username, email=email, telefono=telefono, direccion=direccion,
                                            password=passw, documento=documento, tipo_documento=tipoDoc,
                                            tipo_usuario=tipoU, first_name=nombre, last_name=apellido,
                                            fechaNacimiento=fechaN)
            u.save()
            if tipoU == 'Dueno':
                d = Dueno(documento_id=documento)
            if tipoU == 'Jefe':
                d = Jefe(documento_id=documento, dueno_id=p.documento, asignado=False)
            if tipoU == 'Trabajador':
                d = Trabajador(documento_id=documento, jefe_id=p.documento)
            d.save()
            exito = True
        else:
            errores = form.errors
            if errores.has_key("documento"):
                msn = True
        response = {'msn': msn, 'exito': exito, 'errores': errores}
        return JsonResponse(response)
    else:
        form = PersonaForm()
    return render_to_response('Form_usuario.html', {'user': p, 'tipo_usuario': tipoU, 'form': form},
                              context_instance=RequestContext(request))


@login_required(redirect_field_name=LOGIN_URL)
def crear_cultivo(request):
    user = Persona.objects.get(username=request.user.username)
    # jefes=Jefe.objects.all().filter(dueno_id=user.documento)
    jefes = Jefe.objects.all().filter(Q(dueno_id=user.documento) & Q(asignado=False) & Q(activo=True))

    if request.is_ajax and request.method == 'POST':
        errores = ''
        exito = False

        form = CultivoForm(request.POST)
        if form.is_valid():

            boss = form.cleaned_data['jefe']
            j = Jefe.objects.get(pk=boss.documento)
            j.asignado = True
            j.save()
            temp = form.save(commit=False)
            temp.tipoMedida = 'M2'
            temp.fechaRegsitro = datetime.datetime.now()
            temp.dueno_id = user.documento
            temp.save()

            exito = True
        else:
            errores = form.errors
        response = {'exito': exito, 'errores': errores}
        return JsonResponse(response)
    else:
        form = CultivoForm()
    return render_to_response('Form_Cultivo.html', {'user': user, 'jefes': jefes, 'form': form},
                              context_instance=RequestContext(request))


@login_required(redirect_field_name=LOGIN_URL)
def inicio(request):
    if not request.user.is_superuser:
        user = Persona.objects.get(username=request.user.username)
        return render_to_response('inicio.html', {'user': user})
    else:
        return render_to_response('inicio.html', {'user': request.user})


@login_required(redirect_field_name=LOGIN_URL)
def inf_user(request, cedula):
    if request.user.is_superuser:
        asignaciones = Persona.objects.all().filter(tipo_usuario='Dueno')
        user = request.user
    else:
        user = Persona.objects.get(username=request.user.username)
    persona = Persona.objects.get(username=cedula)
    if persona.tipo_usuario == 'Dueno':
        asignaciones = Cultivo.objects.all().filter(Q(dueno_id=persona.documento) & Q(activo=True))
    if persona.tipo_usuario == 'Jefe':
        asignaciones = Trabajador.objects.all()._next_is_sticky().filter(
            Q(jefe__documento=persona.documento) & Q(activo=True))
    if persona.tipo_usuario == 'Trabajador':
        asignaciones = Lote.objects.all().filter(trabajador_id=persona.documento)
    return render_to_response('inf_usuario.html', {'persona': persona, 'user': user, 'asignaciones': asignaciones})


@login_required(redirect_field_name=LOGIN_URL)
def editar_usuario(request, cedula):
    if request.user.is_superuser:
        user = request.user
    else:
        user = Persona.objects.get(username=request.user.username)
    p = Persona.objects.get(documento=cedula)
    if request.method == 'GET':
        form = EditarPersonaForm(initial={
            'first_name': p.first_name,
            'last_name': p.last_name,
            'telefono': p.telefono,
            'direccion': p.direccion,
            'email': p.email,
            'documento': p.documento,
            'tipo_documento': p.tipo_documento,
            'fechaNacimiento': p.fechaNacimiento,

        })
    if request.method == 'POST':
        form = EditarPersonaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['first_name']
            apellido = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            direccion = form.cleaned_data['direccion']
            fechaN = form.cleaned_data['fechaNacimiento']
            p.first_name = nombre
            p.last_name = apellido
            p.email = email
            p.direccion = direccion
            p.telefono = telefono
            p.fechaNacimiento = fechaN
            p.save()
            return redirect('/personas')
    ctx = {'persona': p, 'user': user, 'tipo_usuario': p.tipo_usuario, 'form': form}
    return render_to_response('editar_usuario.html', ctx, context_instance=RequestContext(request))


@login_required(redirect_field_name=LOGIN_URL)
def eliminar_usuario(request, cedula):
    if request.user.is_superuser:
        user = request.user
    else:
        user = Persona.objects.get(username=request.user.username)
    p = Persona.objects.get(documento=cedula)
    if request.method == 'GET':
        p.is_active = False;
        if p.tipo_usuario == 'Dueno':
            d = Dueno.objects.get(documento=cedula)
            d.activo = False
            d.save()
        if p.tipo_usuario == 'Jefe':
            j = Jefe.objects.get(documento=cedula)
            j.activo = False
            j.save()
        if p.tipo_usuario == 'Trabajador':
            t = Trabajador.objects.get(documento=cedula)
            t.activo = False
            t.save()
        p.save();
    return redirect('/personas');


@login_required(redirect_field_name=LOGIN_URL)
def eliminar_cultivo(request, id_cultivo):
    if request.user.is_superuser:
        user = request.user
    else:
        user = Persona.objects.get(username=request.user.username)
    c = Cultivo.objects.get(id=id_cultivo)
    if request.method == 'GET':
        c.activo = False;
        c.save()
    return redirect('/informacion/usuario/' + user.username);


@login_required(redirect_field_name=LOGIN_URL)
def editar_cultivo(request, id_cultivo):
    if request.user.is_superuser:
        user = request.user
    else:
        user = Persona.objects.get(username=request.user.username)
    c = Cultivo.objects.get(id=id_cultivo)
    jefes = Jefe.objects.all().filter(Q(dueno_id=user.documento) & Q(asignado=False))
    if request.method == 'GET':
        form = EditarCultivoForm(initial={
            'area': c.area,
            'lotes': c.lotes,
        })
    if request.method == 'POST':
        form = EditarCultivoForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data['area']
            lotes = form.cleaned_data['lotes']
            boss = form.cleaned_data['jefe']
            j = Jefe.objects.get(pk=boss.documento)
            j.asignado = True
            if c.jefe != boss:
                j2 = Jefe.objects.get(documento=c.jefe.documento)
                j2.asignado = False
                j2.save()
            c.area = area
            c.lotes = lotes
            c.jefe = boss
            j.save()
            c.save()
            return redirect('/informacion/usuario/' + user.username)
    ctx = {'user': user, 'jefes': jefes, 'form': form}
    return render_to_response('editar_cultivo.html', ctx, context_instance=RequestContext(request))


@login_required(redirect_field_name=LOGIN_URL)
def inf_cultivo(request, id_cultivo):
    if request.user.is_superuser:
        user = request.user
    else:
        user = Persona.objects.get(username=request.user.username)
    cultivo = Cultivo.objects.get(id=id_cultivo)
    return render_to_response('inf_cultivo.html', {'cultivo': cultivo, 'user': user})
