from django.db import models

from django.contrib.auth.models import User



class Persona(User):
	TIPO_DOCUMENTO=(('CC','Cedula Ciudadania'),('CE','Cedula Extrangera'))
	documento=models.CharField(max_length=20,primary_key=True)
	tipo_documento=models.CharField(max_length=20,choices=TIPO_DOCUMENTO)
	tipo_usuario=models.CharField(max_length=20)
	#nombre=models.CharField(max_length=20)
	#apellidos=models.CharField(max_length=20,null=True)
	telefono=models.CharField(max_length=20,null=True)
	direccion=models.CharField(blank=True,max_length=30,null=True)
	#passw=models.CharField(max_length=20)
	#fechaRegistro=models.DateField(default=date.today())
	fechaNacimiento=models.DateField(null=True)



class Dueno(models.Model):
	documento=models.OneToOneField(Persona,primary_key=True)
	def __str__(self):
		return ' %s'%(self.documento.first_name)


class Jefe(models.Model):
	documento=models.OneToOneField(Persona,primary_key=True)
	dueno=models.ForeignKey(Dueno)
	def __str__(self):
		return '%s'%(self.documento.first_name)

class Trabajador(models.Model):
	documento=models.OneToOneField(Persona,primary_key=True)
	jefe=models.ForeignKey(Jefe)
	def __str__(self):
		return '%s'%(self.documento.first_name)

class Cultivo(models.Model):
	
	dueno=models.ForeignKey(Dueno)
	area=models.IntegerField()
	tipoMedida=models.CharField(max_length=3)
	fechaRegsitro=models.DateField()
	jefe=models.OneToOneField(Jefe)
	def __str__(self):
		return '%s %s'%(self.dueno.documento.first_name,self.jefe.documento.first_name)

class Lote(models.Model):
	cultivo=models.ForeignKey(Cultivo)
	area=models.IntegerField()
	tipoMedida=models.CharField(max_length=3)
	totalEstacas=models.IntegerField()
	fechaRegsitro=models.DateField()
	trabajador=models.ForeignKey(Trabajador)
	def __str__(self):
		return '%s %s'%(self.cultivo.dueno.documento.first_name,self.trabajador.documento.first_name)
