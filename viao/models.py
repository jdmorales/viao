from django.db import models

from django.contrib.auth.models import User



class Persona(User):
	TIPO_DOCUMENTO=(('CC','Cedula Ciudadania'),('CE','Cedula Extrangera'))
	documento=models.CharField(max_length=20,primary_key=True)
	tipo_documento=models.CharField(max_length=20,choices=TIPO_DOCUMENTO)
	tipo_usuario=models.CharField(max_length=10)
	#nombre=models.CharField(max_length=20)
	#apellidos=models.CharField(max_length=20,null=True)
	telefono=models.CharField(max_length=20,null=True)
	direccion=models.CharField(blank=True,max_length=20,null=True)
	#passw=models.CharField(max_length=20)
	#fechaRegistro=models.DateField(default=date.today())
	fechaNacimiento=models.DateField(null=True)



class Dueno(models.Model):
	documento=models.ForeignKey(Persona)
	def __str__(self):
		return ' %s'%(self.documento)


class Jefe(models.Model):
	documento=models.ForeignKey(Persona)
	dueno=models.ForeignKey(Dueno)
	def __str__(self):
		return '%s'%(self.documento)

class Trabajador(models.Model):
	documento=models.ForeignKey(Persona)
	jefe=models.ForeignKey(Jefe)
	def __str__(self):
		return '%s'%(self.documento)

class Cultivo(models.Model):
	
	dueno=models.ForeignKey(Dueno)
	area=models.IntegerField()
	tipoMedida=models.CharField(max_length=3)
	fechaRegsitro=models.DateField()
	jefe=models.OneToOneField(Jefe)
	def __str__(self):
		return '%s %s'%(self.dueno.documento.nombre,self.jefe.documento.nombre)

class Lote(models.Model):
	cultivo=models.ForeignKey(Cultivo)
	area=models.IntegerField()
	tipoMedida=models.CharField(max_length=3)
	totalEstacas=models.IntegerField()
	fechaRegsitro=models.DateField()
	trabajador=models.ForeignKey(Trabajador)
	def __str__(self):
		return '%s %s'%(self.cultivo.dueno.documento.nombre,self.trabajador.documento.nombre)
