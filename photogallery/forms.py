#encoding: utf-8
from django import forms
from django.forms import ModelForm
from models import *


class GalleryForm(ModelForm):

	class Meta:
		model = Gallery
		exclude = ('hits','slug')

class ImageForm(ModelForm):

	class Meta:
		model = Image

		widgets = {
			'media_type': forms.RadioSelect(choices=media_types)
		}
