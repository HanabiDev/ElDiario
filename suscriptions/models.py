#encoding: utf-8

from django.db import models

# Create your models here.

class Suscription(models.Model):

	first_name = models.CharField(verbose_name=u'Nombres', max_length=50)
	last_name = models.CharField(verbose_name=u'Apellidos', max_length=50)
	dni = models.CharField(unique=True, verbose_name=u'Documento de Identidad', max_length=15)
	phone = models.CharField(verbose_name=u'Teléfono', max_length=10, blank=True, null=True)
	mobile = models.CharField(verbose_name=u'Teléfono móvil', max_length=13)
	email = models.EmailField(verbose_name=u'Correo Electrónico')
	address = models.CharField(verbose_name=u'Dirección', max_length=50)
	city = models.CharField(verbose_name=u'Ciudad', max_length=30)
	suscription_date = models.DateField(verbose_name=u'Fecha de suscripción', blank=True, null=True)
	suscription_end_date = models.DateField(verbose_name=u'Fin de la suscripción', blank=True, null=True)
	status = models.BooleanField(verbose_name=u'Suscripción activa', default=False)
