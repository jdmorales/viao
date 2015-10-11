from django.db import models

# Create your models here.
class Persona(models.Model):
	TIPO_DOCUMENTO = (
		('TI','Tarjeta de identidad'),
		('CC','Cedula de ciudadania'),
	)
	documento=models.CharField(max_length=20, primary_key=True)
	tipo_documento=models.CharField(max_length=2,choices=TIPO_DOCUMENTO)
	nombre=models.CharField(max_length=20)
	apellidos=models.CharField(max_length=20)
	telefono=models.CharField(max_length=20)
	direccion=models.CharField(max_length=20)
	passw=models.CharField(max_length=20)
	fechaRegistro=models.DateField()
	fechaNacimiento=models.DateField()

	def __str__(self):
		return '%s %s %s'%(self.tipo_documento,self.documento,self.nombre)


class Dueno(models.Model):
	
	documento=models.ForeignKey(Persona)
	perfil=models.CharField(max_length=10)
	def __str__(self):
		return '%s %s'%(self.documento.nombre,self.perfil)


class Jefe(models.Model):
	
	documento=models.ForeignKey(Persona)
	perfil=models.CharField(max_length=10)
	dueno=models.ForeignKey(Dueno)
	def __str__(self):
		return '%s %s'%(self.documento.nombre,self.perfil)

class Trabajador(models.Model):
	
	documento=models.ForeignKey(Persona)
	perfil=models.CharField(max_length=10)
	jefe=models.ForeignKey(Jefe)
	def __str__(self):
		return '%s %s'%(self.documento.nombre,self.perfil)

class Cultivo(models.Model):
	
	dueno=models.ForeignKey(Dueno)
	area=models.IntegerField()
	tipoMedida=models.CharField(max_length=3)
	fechaRegsitro=models.DateField()
	jefe=models.ForeignKey(Jefe)
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