#encoding: utf-8
from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

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
		('7','7: Derecha Arriba (275x300)'),
		('8','8: Derecha Abajo (275x90)'),
	)

	AD_TYPES = (
		('1', 'Animación'),
		('2', 'Imagen'),
		('3', 'Video'),
	)

	title = models.CharField(verbose_name=u'Título', max_length=100, unique=True)
	ad_type = models.CharField(verbose_name=u'Tipo', choices=AD_TYPES, max_length=10)
	pkg_file = models.FileField(verbose_name=u'Archivo', upload_to='uploads/ads/zipped', default='No File')
	embed_code = models.TextField(verbose_name=u'Código HTML', default='Insertar HTML', blank=True)
	position = models.CharField(verbose_name=u'Posición', choices=POSITION_INDEXES, max_length=30)
	creation_date = models.DateField(auto_now=True)
	published = models.BooleanField(default=True, verbose_name=u'Publicado')
	

	def save(self, *args, **kwargs):
		

		if not self.id:
			super(Ad, self).save(*args, **kwargs)
			if self.ad_type == '3':
				unzip_pkg(self.position, self.embed_code, self.ad_type)
			else:
				unzip_pkg(self.position, self.pkg_file, self.ad_type)
		else:
			this = Ad.objects.get(id=self.id)

			if this.pkg_file != self.pkg_file:
				this.pkg_file.delete(save=False)


			super(Ad, self).save(*args, **kwargs)
			publish_files(self)


	def delete(self, *args, **kwargs):
		self.pkg_file.delete()
		clean_files(self.position)

		super(Ad, self).delete(*args, **kwargs)





import glob
import re
import codecs

def unzip_pkg(pos, pkg, ad_type):

	if pkg:

		if ad_type == '2':
			path = os.path.join(settings.MEDIA_ROOT,'uploads/ads/pos'+pos)
			template = open(path+'/template_index.html', 'w+')

			image = '<img src="'+settings.MEDIA_URL+pkg.name+'"/>'
			template.write(image)
			template.flush()
			template.close()

		elif ad_type == '1':

			#Path to unzip contents
			unzip_path = os.path.join(settings.MEDIA_ROOT,'uploads/ads/pos'+pos)
			#File to unzip
			zfile = zipfile.ZipFile(pkg)
			
			#Delete target directory
			shutil.rmtree(unzip_path)
			
			#Make target directory
			os.makedirs(unzip_path)
			#Unzip
			zfile.extractall(unzip_path)

			#open uploaded edgePreload.js and modify to include static urls
			

			preload_file = codecs.open(glob.glob(unzip_path+'/*edgePreload.js')[0], encoding='utf-8')
			
			s=preload_file.read()
			s=re.sub(r'edge_includes', '/static/js/edge_includes', s)
			s=re.sub(r'"([\w.-]{0,}js)"', r'"/media/uploads/ads/pos'+pos+r'/\1"', s)
			
			f=open(glob.glob(unzip_path+'/*edgePreload.js')[0], 'w')
			f.write(s)
			f.flush()
			f.close()


			preload_file = codecs.open(glob.glob(unzip_path+'/*_edge.js')[0], encoding='utf-8')
			
			s=preload_file.read()
			s=re.sub(r'(images\/)', r'/media/uploads/ads/pos'+pos+r'/\1', s)
			
			f=open(glob.glob(unzip_path+'/*_edge.js')[0], 'w')
			f.write(s)
			f.flush()
			f.close()

			

			preload_file = codecs.open(glob.glob(unzip_path+'/*.html')[0], encoding='utf-8')
			
			s=preload_file.read()


			s=re.sub(r'"([\w.-]{0,}js)"', r'"/media/uploads/ads/pos'+pos+r'/\1"', s)

			#Open *.html and replace imported library paths
			f=codecs.open(glob.glob(unzip_path+'/*.html')[0], encoding='utf-8', mode='w+')
			
			f.write(s)
			f.flush()
			f.close()


			path = os.path.join(settings.MEDIA_ROOT,'uploads/ads/pos'+pos)
			template = open(path+'/template_index.html', 'w+')

			include = '{% include "pos'+pos+'/index.html" %}'
			template.write(include)
			template.flush()
			template.close()
		else:
			path = os.path.join(settings.MEDIA_ROOT,'uploads/ads/pos'+pos)
			template = open(path+'/template_index.html', 'w+')

			template.write(pkg)
			template.flush()
			template.close()

def clean_files(pos):
	#Path to unzip contents
	files_path = os.path.join(settings.MEDIA_ROOT,'uploads/ads/pos'+pos+'/')
	
	#Delete target directory
	shutil.rmtree(files_path)
	os.makedirs(files_path)

	template = open(files_path+'/template_index.html', 'w+')

	template.write("")
	template.flush()
	template.close()

def publish_files(ad):
	if ad.published:
		if ad.ad_type == '3':
			unzip_pkg(ad.position, ad.embed_code, ad.ad_type)
		else:
			unzip_pkg(ad.position, ad.pkg_file, ad.ad_type)
	else:
		clean_files(ad.position)

	

		
