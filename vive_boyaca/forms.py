from django import forms
from models import *

class TownForm(forms.ModelForm):

	class Meta:
		model = Town
		exclude = ('slug',)

class POIForm(forms.ModelForm):

	class Meta:
		model = PointOfInterest