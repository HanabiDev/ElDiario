from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from content.models import *
from polls.models import *
from photogallery.models import *
# Create your views here.
from datetime import datetime

TEMPLATE_DIR = 'frontend/../'
def home(request):

	if request.GET.get('launched')=='True':
		request.session["launch"]=True
		return redirect('/')



	full_width_article = None
	poll = None
	new_suscriptions = None
	gallery = None
	carousel_images = None
	order = None

	try:
		full_width_article = Article.objects.get(full_width=True)
		poll = Poll.objects.get(closed=False)
		gallery = Gallery.objects.all().order_by('-creation_date')[0]
		carousel_images = gallery.images.all()
		order = range(0,len(carousel_images))


	except Exception, e:
		pass

	categories = Category.objects.filter(parent=None, published=True)
	count = Article.objects.filter(full_width=False, published=True).count()
	if count > 0:
		main_art = Article.objects.filter(full_width=False, published=True).order_by('-creation_date')[0]
		all_articles = Article.objects.filter(full_width=False, published=True).order_by('-creation_date')[1:5]
	else:
		main_art = None
		all_articles = None

	return render_to_response(TEMPLATE_DIR+'site_index.html',
		{'full_width_article': full_width_article, 'poll':poll, 'articles':all_articles,
		 'categories': categories, 'main_art':main_art, 'images':carousel_images, 'gallery':gallery, 'order':order},
		context_instance=RequestContext(request)
	)

def serve_article(request, slug):
	article = get_object_or_404(Article, slug=slug)
	article.hits = article.hits + 1
	article.save()
	categories = Category.objects.filter(parent=None, published=True)

	return render_to_response(TEMPLATE_DIR+'article.html', {'article':article, 'categories':categories})

def serve_category(request, slug):
	if slug == "general":
		category = None
	else:
		category = get_object_or_404(Category, slug=slug)

	articles = Article.objects.filter(category=category).order_by('-creation_date')
	categories = Category.objects.filter(parent=None, published=True)

	return render_to_response(TEMPLATE_DIR+'category.html', {'articles':articles, 'category':category, 'categories':categories})

def serve_gallery(request, slug):
	gallery = get_object_or_404(Gallery, slug=slug)
	gallery.hits = gallery.hits + 1
	gallery.save()
	categories = Category.objects.filter(parent=None, published=True)

	return render_to_response(TEMPLATE_DIR+'gallery.html',
		{'gallery':gallery, 'categories':categories, 'images':gallery.images.all(), 'order':range(0,len(gallery.images.all()))})


def impressed(request):
	categories = Category.objects.filter(parent=None, published=True)
	return render_to_response(TEMPLATE_DIR+'impressed.html', {'categories':categories})
