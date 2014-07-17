from django import template
register = template.Library()

from content.models import *

def get_position_article(position_label):

  category = Category.objects.filter(main_page_position=position_label)
  art_excluded = Article.objects.filter(full_width=False, published=True).order_by('-creation_date').values('id')[:6]

  article = None
  try:
    article = Article.objects.filter(category=category, published=True).exclude(full_width=False,id__in=art_excluded).order_by('-creation_date')
  except Exception as e:
    return article

  if position_label == "S":
    if len(article)>=2:
      article = article[:2]
  else:
    if len(article)>=1:
      article = article[0]

  return article

register.filter('get_position_article', get_position_article)
