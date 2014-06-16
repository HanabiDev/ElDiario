#encoding: utf-8
from django import forms
from models import *
class AdForm(forms.ModelForm):

	class Meta:

		AD_TYPES = (
			('1', 'Imagen'),
			('2', 'Animación'),
			('3', 'Video'),
		)


		model = Ad
		exclude = ('path',)

		widgets = {
			'ad_type': forms.RadioSelect(choices=AD_TYPES)
		}