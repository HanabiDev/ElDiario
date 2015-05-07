#encoding: utf-8
from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

from content.models import Category

# Create your models here.

import os
import zipfile
import shutil

class Ad(models.Model):

	POSITION_INDEXES = (
		('1','1: Pre Encabezado (1080x160)'),
		('2','2: Externa Izquierda (134x660)'),
		('3','3: Externa Derecha (134x660)'),
		('4','4: Post Encabezado 1080x90'),
		('5','5: Pre Principales (710x120)'),
		('6','6: Post Principales (710x160)'),
		('7','7: Derecha Arriba A (275x300)'),
		('8','8: Derecha Arriba B (275x90)'),
		('9','9: Derecha Abajo (275x300)'),
		('10','10: Post Twitter (275 de ancho)'),
		('11','11: Móvil'),
	)

	AD_TYPES = (
		('1', 'Animación'),
		('2', 'Imagen'),
		('3', 'Video/HTML'),
	)

	title = models.CharField(verbose_name=u'Título', max_length=100, unique=True)
	ad_type = models.CharField(verbose_name=u'Tipo', choices=AD_TYPES, max_length=10)
	ad_file = models.FileField(verbose_name=u'Archivo', upload_to='uploads/ads/zipped', default='No File')
	embed_code = models.TextField(verbose_name=u'Código HTML', default='Insertar HTML', blank=True)
	position = models.CharField(verbose_name=u'Posición', choices=POSITION_INDEXES, max_length=30)
	creation_date = models.DateField(auto_now=True)
	published = models.BooleanField(default=True, verbose_name=u'Publicado')
	categories = models.ManyToManyField(Category, verbose_name='Categorías relacionadas')

	def save(self, *args, **kwargs):
		if not self.id:
			super(Ad, self).save(*args, **kwargs)
		
		if not (self.position == "10" or self.position == "11"):
			Ad.objects.filter(
				position=self.position
			).exclude(id=self.id).update(published=False)
		
		super(Ad, self).save(*args, **kwargs)
