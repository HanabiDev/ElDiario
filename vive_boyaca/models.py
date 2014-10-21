#encoding: utf-8
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Town(models.Model):

	def get_cover_path(self, filename):
		return 'uploads/vive_boyaca/%s/%s' % (self.slug, filename)

	slug = models.SlugField(unique=True, blank=True, max_length=150)
	cover_image = models.ImageField(upload_to=get_cover_path, verbose_name=u'Imagen de Portada')
	name = models.CharField(verbose_name=u'Nombre', max_length=100, unique=True)
	province = models.CharField(verbose_name=u'Provincia', max_length=500)
	slogan = models.CharField(verbose_name=u'Lema', max_length=500, null=True, blank=True)
	phone = models.CharField(verbose_name=u'Teléfono', max_length=40)
	address = models.CharField(verbose_name=u'Dirección', max_length=100)
	email = models.EmailField(verbose_name=u'Correo Electrónico', max_length=100, unique=True)
	website = models.URLField(verbose_name=u'Sitio Web', unique=True)
	mayor = models.CharField(verbose_name=u'Alcalde', max_length=200)
	mayor_pic = models.ImageField(upload_to=get_cover_path, verbose_name=u'Foto Alcalde')
	gov_period = models.CharField(verbose_name=u'Período de Gobierno', max_length=100)
	published = models.BooleanField(verbose_name=u'Publicado', default=True)
	report = models.URLField(verbose_name=u'URL Reporte de Gestión', blank=True, null=True)
	main_page = models.BooleanField(default=False, verbose_name=u'Página principal')

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		if self.main_page:
			Town.objects.all().update(main_page=False)
			self.main_page = True

		super(Town, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "municipio"

POINT_TYPES = (
	('1', 'Turístico'),
	('2', 'Restaurante'),
	('3', 'Hotel'),
)

class PointOfInterest(models.Model):
	town = models.ForeignKey(Town, verbose_name=u'Municipio')
	name = models.CharField(verbose_name=u'Nombre', max_length=100, unique=True)
	point_type = models.CharField(verbose_name=u'Tipo', max_length=1, choices=POINT_TYPES, default='1')
	address = models.CharField(verbose_name=u'Dirección', max_length=100)
	phone = models.CharField(verbose_name=u'Teléfono', max_length=20, null=True, blank=True)
	mobile = models.CharField(verbose_name=u'Móvil', max_length=20, null=True, blank=True)

