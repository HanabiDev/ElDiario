#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from content.models import Category
from redactor.fields import RedactorField
# Create your models here.

media_types = (
	('video','video'),
	('url','url'),
	('image','image'),
)

class Gallery(models.Model):
	title = models.CharField(verbose_name=u'Título', max_length=100, unique=True)
	description = RedactorField(verbose_name=u'Descripción', blank=True)
	creation_date = models.DateField(auto_now=True)
	published = models.BooleanField(verbose_name=u'Publicada', default=True)
	author = models.ForeignKey(User, verbose_name=u'Autor')
	category = models.ForeignKey(Category, verbose_name=u'Categoría', null=True, blank=True)
	hits = models.IntegerField(default=0)
	images = models.ManyToManyField('Image', related_name='gallery', null=True, blank=True)

class Image(models.Model):
	image_title = models.CharField(verbose_name=u'Título de la imagen', max_length=100)
	description = models.TextField(verbose_name=u'Descripción', blank=True)
	media_type = models.CharField(choices=media_types, max_length=5)
	image = models.ImageField(verbose_name=u'Archivo de Imagen', upload_to='uploads/galleries',blank=True, null=True)
	url = models.URLField(default='', blank=True, null=True)
	code = models.TextField(default='', blank=True, null=True)
	author = models.CharField(verbose_name=u'Fotógrafo', max_length=100, blank=True)
	capture_datetime = models.DateTimeField(verbose_name='Fecha de captura', blank=True, auto_now=True)

	def __str__(self):
		return str(self.image)

class GalleryImage(models.Model):
	image = models.ForeignKey(Image)
	gallery = models.ForeignKey(Gallery)
