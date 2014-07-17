#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from redactor.fields import RedactorField
from django.template.defaultfilters import slugify
from datetime import datetime as date

MAIN_PAGE_POSITIONS = (
	('S','Secundarias destacado'),
	('A','Otras A'),
	('B','Otras B'),
	('C','Otras C'),
	('D','Otras D'),
	('E','Otras E'),
	('F','Otras F'),
	('G','Otras G'),
	('H','Otras H'),
	('I','Otras I'),
	('J','Otras J'),
	('R','Derecha'),
)

class Category(models.Model):
	slug = models.SlugField(unique=True, blank=True, max_length=150)
	title = models.CharField(max_length=50, verbose_name=u'Título', unique=True)
	description = RedactorField(verbose_name=u'Descripción', blank=True)
	creation_date = models.DateField(auto_now=True)
	author = models.ForeignKey(User, verbose_name=u'Autor')
	published = models.BooleanField(default=True, verbose_name=u'Publicada')
	parent = models.ForeignKey('Category',verbose_name='Padre', related_name='parent_cat', null=True, blank=True)
	main_page_position = models.CharField(
		max_length=1, null=True, blank=True,
		verbose_name=u'Posición en la página de inicio', choices=MAIN_PAGE_POSITIONS
	)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

class Article(models.Model):
	slug = models.SlugField(unique=True, blank=True)
	title = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
	abstract = RedactorField(verbose_name=u'Resumen')
	content = RedactorField(verbose_name=u'Contenido')
	creation_date = models.DateTimeField(default=date.now)
	author = models.ForeignKey(User, verbose_name=u'Autor')
	category = models.ForeignKey(Category, verbose_name=u'Categoría', null=True, blank=True)
	published = models.BooleanField(default=True, verbose_name=u'Publicado')
	featured = models.BooleanField(default=True, verbose_name="Destacado")
	hits = models.IntegerField(default=0)
	full_width = models.BooleanField(default=False, verbose_name='Ancho completo')
	related_articles = models.ManyToManyField('Article', verbose_name=u'Artículos relacionados', related_name='related', null=True, blank=True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)
