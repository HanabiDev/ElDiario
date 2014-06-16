#encoding: utf-8
from django.db import models

# Create your models here.

class Poll(models.Model):
	poll_title = models.CharField(max_length=50, verbose_name=u'Título')
	poll_question = models.CharField(max_length=150, verbose_name=u'Pregunta')
	creation_date = models.DateField(auto_now=True)
	closed = models.BooleanField(verbose_name=u'Cerrada')

class Option(models.Model):
	question_text = models.CharField(max_length=100, verbose_name=u'Texto de la opción')
	order = models.IntegerField()
	poll = models.ForeignKey(Poll, verbose_name=u'Encuesta')

class Vote(models.Model):
	poll = models.ForeignKey(Poll)
	option = models.ForeignKey(Option)
	hits = models.IntegerField()
