from django import forms
from viao.models import Persona
from django.contrib.auth.models import User


class PersonaForm(forms.ModelForm):
   class Meta:
      model = Persona
      fields = ['tipo_documento','documento','tipo_usuario', 'telefono','direccion', 'fechaNacimiento', 'username', 'first_name', 'last_name', 'email','password']
      widgets = {
           'password': forms.PasswordInput(),
      }