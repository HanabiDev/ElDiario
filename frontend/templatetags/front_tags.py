from django import template
register = template.Library()

from content.models import *

def get_position_article(position_label):

  category = Category.objects.filter(main_page_position=position_label)
  art_excluded = None

  article = None

  try:
    articles = Article.objects.exclude(full_width=True, published=False).order_by('-creation_date')
    articles = articles.filter(category=category).order_by('-creation_date')

    if position_label=="S":
      article = articles[0:2]
    else:
      article = articles[0]

    except Exception as e:
      return article
  return article

register.filter('get_position_article', get_position_article)
