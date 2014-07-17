#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from content.models import Category
from redactor.fields import RedactorField
from django.template.defaultfilters import slugify
# Create your models here.

media_types = (
	('i','Imagen'),
	('u','URL'),
	('v','Video')
)

class Gallery(models.Model):
	slug = models.SlugField(unique=True, blank=True)
	title = models.CharField(verbose_name=u'Título', max_length=100, unique=True)
	description = RedactorField(verbose_name=u'Descripción', blank=True)
	creation_date = models.DateField(auto_now=True)
	published = models.BooleanField(verbose_name=u'Publicada', default=True)
	author = models.ForeignKey(User, verbose_name=u'Autor')
	category = models.ForeignKey(Category, verbose_name=u'Categoría', null=True, blank=True)
	hits = models.IntegerField(default=0)
	images = models.ManyToManyField('Image', related_name='gallery', null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Gallery, self).save(*args, **kwargs)

class Image(models.Model):
	image_title = models.CharField(verbose_name=u'Título', max_length=100)
	media_type = models.CharField(verbose_name=u'Tipo', choices=media_types, max_length=5)
	image = models.ImageField(verbose_name=u'Archivo de Imagen', upload_to='uploads/galleries',blank=True, null=True)
	url = models.URLField(default='', blank=True, null=True, verbose_name=u'URL')
	code = models.TextField(verbose_name=u'Código Embebido', default='', blank=True, null=True)
	description = models.TextField(verbose_name=u'Descripción', blank=True)
	author = models.CharField(verbose_name=u'Fotógrafo', max_length=100, blank=True)
	capture_datetime = models.DateTimeField(verbose_name='Fecha de captura', blank=True, auto_now=True)

	def __str__(self):
		return str(self.image_title)
