from django import template
register = template.Library()

from ads.models import *

def get_ad(index):

  	ad = None
  	index = index/2
  	
	try:
		ad = Ad.objects.filter(position='11', published=True).order_by('-creation_date')[index]
	except Exception as e:
		pass
	  
	return ad

register.filter('get_ad', get_ad)
