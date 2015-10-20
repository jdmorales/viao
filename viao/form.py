from django import forms
from viao.models import Persona,Cultivo
from django.contrib.auth.models import User


class PersonaForm(forms.ModelForm):
   class Meta:
      model = Persona
      fields = ['tipo_documento','documento', 'telefono','direccion', 'fechaNacimiento', 'first_name', 'last_name', 'email','password']
      widgets = {
           'password': forms.PasswordInput(),
      }
      
class CultivoForm(forms.ModelForm):
   class Meta:
      model = Cultivo
      fields = ['area','jefe']
      
      