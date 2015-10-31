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
        print documento
        if not documento.isdigit():
            raise forms.ValidationError("Not is valid!")
        return documento
  def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        print telefono
        if not telefono.isdigit():
            raise forms.ValidationError("Not is valid!")
        return telefono

  def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        print first_name
        if first_name.isdigit():
            raise forms.ValidationError("Not is valid!")
        return first_name

  def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        print last_name
        if last_name.isdigit():
            raise forms.ValidationError("Not is valid!")
        return last_name


class CultivoForm(forms.ModelForm):
	class Meta:
		model = Cultivo
		fields = ['area','jefe','lotes']
		widgets={
			'area':forms.NumberInput(attrs={'placeholder':'Area','class':'form-control input-lg','min': 5 , 'max': 20}),
            'lotes':forms.NumberInput(attrs={'placeholder':'Cantidad de lotes','class':'form-control input-lg'}),

		}
	#def __init__(self,*args,**kwargs):
	#	self.user = kwargs.pop('user',None) 
	#	super(CultivoForm,self).__init__(*args,**kwargs)
	#	self.fields['jefe'].queryset = Jefe.objects.filter(dueno_id=self.user)



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
 
  def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        print telefono
        if not telefono.isdigit():
            raise forms.ValidationError("Not is valid!")
        return telefono

  def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        print first_name
        if first_name.isdigit():
            raise forms.ValidationError("Not is valid!")
        return first_name

  def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        print last_name
        if last_name.isdigit():
            raise forms.ValidationError("Not is valid!")
        return last_name














