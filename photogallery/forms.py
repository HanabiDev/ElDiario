from django.forms import ModelForm
from models import *


class GalleryForm(ModelForm):
	
	class Meta:
		model = Gallery
		exclude = ('hits',)

class ImageForm(ModelForm):
	
	class Meta:
		model = Image