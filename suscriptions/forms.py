from models import *
from django import forms

class SuscriptionForm(forms.ModelForm):

	class Meta:
		model = Suscription
