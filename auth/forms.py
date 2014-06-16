#encoding:utf-8
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from django.contrib.auth.models import User, Group
from django import forms


class UserAddForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = "Usuario"
		self.fields['password1'].label = "Contraseña"
		self.fields['password2'].label = "Confirmar contraseña"




class UserEditForm(UserChangeForm):
	def __init__(self, *args, **kwargs):
		super(UserChangeForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = "Usuario"
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True


	class Meta:
		
		model = User
		fields = ['first_name', 'last_name', 'username', 'password', 'email', 'is_superuser', 'is_active', 'is_staff','user_permissions', 'groups']

		labels = {
            'username': 'Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
            'is_superuser': 'Superusuario',
            'is_active': 'Activo',
            'user_permissions': 'Permisos',
            'groups': 'Grupos',
            'password': '',
            'is_staff': 'Administrador'
        }

class ChangePassForm(AdminPasswordChangeForm):

	def __init__(self, *args, **kwargs):
		super(AdminPasswordChangeForm, self).__init__(*args, **kwargs)
		self.fields['password1'].label = "Nueva contraseña"
		self.fields['password2'].label = "Confirmar nueva contraseña"


class GroupAddForm(forms.ModelForm):

	class Meta:
		model = Group





