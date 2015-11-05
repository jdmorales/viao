from django import forms
from viao.models import Persona,Jefe,Dueno,Trabajador,Cultivo,Lote
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['tipo_documento','documento', 'telefono','direccion', 'fechaNacimiento', 'first_name', 'last_name', 'email','password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control input','placeholder':'Contrasena'}),
            'fechaNacimiento':forms.DateInput(attrs={'class':'form-control input','placeholder':'yyyy-mm-dd'}),
            'email':forms.EmailInput(attrs={'class':'form-control input','placeholder':'example@mail.com'}),
            'documento':forms.TextInput(attrs={'class':'form-control input','placeholder':'Numero de documento'}),
            'telefono':forms.TextInput(attrs={'class':'form-control input','placeholder':'Numero de telefono'}),
            'tipo_documento':forms.Select(attrs={'class':'form-control input'}),
            'first_name':forms.TextInput(attrs={'class':'form-control input','placeholder':'Nombre'}),
            'last_name':forms.TextInput(attrs={'class':'form-control input','placeholder':'Apellidos'}),
            'direccion':forms.TextInput(attrs={'class':'form-control input','placeholder':'Direccion'}),
        }

    #labels = {
      #"documento": _("hola!"),
    #}
    def clean_documento(self):
            documento = self.cleaned_data.get('documento')
            if not documento.isdigit():
                raise forms.ValidationError("Not is valid!")
            return documento
    def clean_telefono(self):
            telefono = self.cleaned_data.get('telefono')
            if not telefono.isdigit():
                raise forms.ValidationError("Not is valid!")
            return telefono

    def clean_first_name(self):
            booleano = False
            first_name = self.cleaned_data.get('first_name')
            for x in first_name:
                if x.isdigit():
                    booleano=True
            if first_name=="" or booleano:
                raise forms.ValidationError("Not is valid!")
            return first_name

    def clean_last_name(self):
            booleano = False
            last_name = self.cleaned_data.get('last_name')
            for x in last_name:
                if x.isdigit():
                    booleano=True
            if last_name=="" or booleano:
                raise forms.ValidationError("Not is valid!")
            return last_name

    def clean_password(self):
        booleano=True
        password = self.cleaned_data.get('password')
        size=len(password)
        for x in password:
            if x.isdigit():
                booleano=False
        if size <=8 or size >=20 or booleano:
            raise forms.ValidationError("Not is valid!")
        return password


class CultivoForm(forms.ModelForm):
	class Meta:
		model = Cultivo
		fields = ['area','jefe','lotes']
		widgets={
			'area':forms.NumberInput(attrs={'placeholder':'Area','class':'form-control input-lg','min': 5 , 'max': 20}),
            'lotes':forms.NumberInput(attrs={'placeholder':'Cantidad de lotes','class':'form-control input-lg'}),

		}
	def clean_area(self):
            area = self.cleaned_data.get('area')
            if area > 20:
                raise forms.ValidationError("Not is valid!")
            return area
 
	#def __init__(self,*args,**kwargs):
	#	self.user = kwargs.pop('user',None) 
	#	super(CultivoForm,self).__init__(*args,**kwargs)
	#	self.fields['jefe'].queryset = Jefe.objects.filter(dueno_id=self.user)

class EditarCultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = ['area','jefe','lotes']
        widgets={
            'area':forms.NumberInput(attrs={'placeholder':'Area','class':'form-control input-lg','min': 5 , 'max': 20}),
            'lotes':forms.NumberInput(attrs={'placeholder':'Cantidad de lotes','class':'form-control input-lg'}),
        }
    def clean_area(self):
        area = self.cleaned_data.get('area')
        if area > 20:
            raise forms.ValidationError("Not is valid!")
        return area


class EditarPersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['telefono','direccion', 'fechaNacimiento', 'first_name', 'last_name', 'email']
        widgets = {
            
            'fechaNacimiento':forms.DateInput(attrs={'class':'form-control input','placeholder':'yyyy-mm-dd'}),
            'email':forms.EmailInput(attrs={'class':'form-control input','placeholder':'example@mail.com'}),
            'telefono':forms.TextInput(attrs={'class':'form-control input','placeholder':'Numero de telefono'}),
            'first_name':forms.TextInput(attrs={'class':'form-control input','placeholder':'Nombre'}),
            'last_name':forms.TextInput(attrs={'class':'form-control input','placeholder':'Apellidos'}),
            'direccion':forms.TextInput(attrs={'class':'form-control input','placeholder':'Direccion'}),
    
        }

    #labels = {
      #"documento": _("hola!"),
    #}
 
    def clean_documento(self):
            documento = self.cleaned_data.get('documento')
            if not documento.isdigit():
                raise forms.ValidationError("Not is valid!")
            return documento
    def clean_telefono(self):
            telefono = self.cleaned_data.get('telefono')
            if not telefono.isdigit():
                raise forms.ValidationError("Not is valid!")
            return telefono

    def clean_first_name(self):
            booleano = False
            first_name = self.cleaned_data.get('first_name')
            for x in first_name:
                if x.isdigit():
                    booleano=True
            if first_name=="" or booleano:
                raise forms.ValidationError("Not is valid!")
            return first_name

    def clean_last_name(self):
            booleano = False
            last_name = self.cleaned_data.get('last_name')
            for x in last_name:
                if x.isdigit():
                    booleano=True
            if last_name=="" or booleano:
                raise forms.ValidationError("Not is valid!")
            return last_name




    











