from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from content.models import *
from polls.models import *
# Create your views here.

TEMPLATE_DIR = 'frontend/../'
def home(request):

	full_width_article = None
	poll = None
	new_suscriptions = None

	try:
		full_width_article = Article.objects.get(full_width=True)
		poll = Poll.objects.get(closed=False)

	except Exception, e:
		pass

	categories = Category.objects.filter(parent=None)
	count = Article.objects.filter(full_width=False).count()
	if count > 0:
		main_art = Article.objects.filter(full_width=False).order_by('-creation_date')[0]
		all_articles = Article.objects.filter(full_width=False).order_by('-creation_date')[1:5]
	else:
		main_art = None
		all_articles = None

	return render_to_response(TEMPLATE_DIR+'site_index.html',
		{'full_width_article': full_width_article, 'poll':poll, 'articles':all_articles,
		 'categories': categories, 'main_art':main_art},
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
	if slug == "general":
		category = None
	else:
		category = get_object_or_404(Category, slug=slug)

	articles = Article.objects.filter(category=category).order_by('-creation_date')
	categories = Category.objects.filter(parent=None)

	return render_to_response(TEMPLATE_DIR+'category.html', {'articles':articles, 'category':category, 'categories':categories})
