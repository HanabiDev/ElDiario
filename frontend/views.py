from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from content.models import *
# Create your views here.

TEMPLATE_DIR = 'frontend/../'
def home(request):

	full_width_article = None
	try:
		categories = Category.objects.filter(parent=None)
		print len(categories)

		full_width_article = Article.objects.get(full_width=True)
	except Exception, e:
		pass

	all_articles = Article.objects.exclude(full_width=True).order_by('-creation_date')

	return render_to_response(TEMPLATE_DIR+'site_index.html',
		{'full_width_article': full_width_article, 'articles':all_articles, 'categories': categories},
		context_instance=RequestContext(request)
	)

def serve_article(request, slug):
	article = get_object_or_404(Article, slug=slug)
	article.hits = article.hits + 1
	article.save()
	categories = Category.objects.filter(parent=None)
	print article

	return render_to_response(TEMPLATE_DIR+'article.html', {'article':article, 'categories':categories})

def serve_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	articles = Article.objects.filter(category=category).order_by('-creation_date')
	categories = Category.objects.filter(parent=None)

	return render_to_response(TEMPLATE_DIR+'category.html', {'articles':articles, 'category':category, 'categories':categories})
