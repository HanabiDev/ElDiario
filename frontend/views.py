#encoding: utf-8
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.db.models import Q
from content.models import *
from polls.models import *
from vive_boyaca.models import *
from photogallery.models import *
from conf.views import load_settings
# Create your views here.
from datetime import datetime

TEMPLATE_DIR = 'frontend/../'
def home(request):

	full_width_article = None
	try:
		full_width_article = Article.objects.filter(full_width=True, published=True)[0]
	except Exception as e:
		pass

	poll = None
	try:
		poll = Poll.objects.get(closed=False)
	except Exception as e:
		pass

	galleries = None
	order = None
	try:
		galleries = Gallery.objects.filter(published=True).order_by('-creation_date')[0:4]
		carousel_images = galleries[0].images.all()
		order = range(0,len(carousel_images))
	except Exception as e:
		pass

	cartoons = None
	orderCartoons = None
	try:
		cartoons = Article.objects.filter(category__title='Caricaturas', published=True).order_by('-creation_date')
		orderCartoons = range(0,len(cartoons))

	except Exception as e:
		pass

	categories = None
	try:
		categories = Category.objects.filter(parent=None, published=True)
	except Exception as e:
		pass

	main_art = None
	all_articles = None

	settings = load_settings()

	try:
		count = Article.objects.filter(full_width=False, published=True).exclude(category__title='Caricaturas').count()
		if count > 0:
			main_art = Article.objects.filter(
				full_width=False,
				published=True
			).exclude(category__title='Caricaturas').order_by('-creation_date')[0]

			secondary = Article.objects.filter(
				full_width=False, published=True
			).exclude(category__title='Caricaturas').order_by('-creation_date')[1:5]

			misc_news = Article.objects.filter(
				full_width=False, published=True
			).exclude(category__title='Caricaturas').order_by('-creation_date')[6:24]

	except Exception as e:
		pass

	
	
	try:
		opinion_articles = Article.objects.filter(category__parent__title='Columnistas').order_by('-creation_date')[0:8]
		cafe_con = Article.objects.filter(category__title='Un café con').order_by('-creation_date')[0]
		cartas_lector = Article.objects.filter(category__title='Cartas del lector').order_by('-creation_date')[0]
	except Exception, e:
		print e

	return render_to_response(TEMPLATE_DIR+'site_index.html',
		{
			'categories': categories,
			'full_width_article': full_width_article,
			'main_art':main_art,
			'secondary':secondary, 'misc_news':misc_news,
			'poll':poll, 'galleries':galleries,
			'cartoons':cartoons, 'orderCartoons':orderCartoons,
			'settings':settings,
			'opinion_news': opinion_articles,
			'carta': cartas_lector,
			'cafe_con': cafe_con,
		},
		context_instance=RequestContext(request)
	)

def search(request):

	keyword = request.GET.get('keyword')

	if keyword:
		categories = Category.objects.filter(
			Q(title__contains=keyword) | Q(description__contains=keyword)
		).exclude(published=False)

		articles = Article.objects.filter(
			Q(title__contains=keyword) | Q(abstract__contains=keyword) | Q(content__contains=keyword)
		).exclude(published=False)

		galleries = Gallery.objects.filter(
			Q(title__contains=keyword) | Q(description__contains=keyword)
		).exclude(published=False)
		settings = load_settings()
		return render_to_response(TEMPLATE_DIR+'search.html', {'settings':settings, 'keyword':keyword, 'articles':articles, 'categories':categories, 'galleries':galleries})
	else:
		return redirect('/')

def serve_article(request, slug):
	article = get_object_or_404(Article, slug=slug)
	article.hits = article.hits + 1
	article.save()
	categories = Category.objects.filter(parent=None, published=True)
	settings = load_settings()
	return render_to_response(TEMPLATE_DIR+'article.html', {'article':article, 'categories':categories,'settings':settings,})

def serve_category(request, slug):
	if slug == "general":
		category = None
	elif slug == 'vive-boyaca':
		return redirect('/vive-boyaca/')
	else:
		category = get_object_or_404(Category, slug=slug)

	articles = Article.objects.filter(category=category).order_by('-creation_date')
	categories = Category.objects.filter(parent=None, published=True)
	settings = load_settings()

	return render_to_response(TEMPLATE_DIR+'category.html', {'articles':articles, 'category':category, 'settings':settings,'categories':categories})

def serve_gallery(request, slug):
	gallery = get_object_or_404(Gallery, slug=slug)
	gallery.hits = gallery.hits + 1
	gallery.save()
	categories = Category.objects.filter(parent=None, published=True)
	settings = load_settings()
	return render_to_response(TEMPLATE_DIR+'gallery.html',
		{'gallery':gallery, 'categories':categories, 'images':gallery.images.all(), 'settings':settings,'order':range(0,len(gallery.images.all()))})


def impressed(request):
	categories = Category.objects.filter(parent=None, published=True)
	return render_to_response(TEMPLATE_DIR+'impressed.html', {'categories':categories})

def all_articles(request):

	articles = Article.objects.filter(published=True).order_by('-creation_date')
	categories = Category.objects.filter(parent=None, published=True)
	settings = load_settings()

	return render_to_response(TEMPLATE_DIR+'category.html', {'articles':articles, 'settings':settings, 'all_arts':True, 'categories':categories})

def all_cats(request):
	categories = Category.objects.filter(parent=None, published=True)
	settings = load_settings() 
	return render_to_response(TEMPLATE_DIR+'categories.html', {'all_arts':True, 'settings':settings, 'categories':categories})

def serve_town(request, slug):
	categories = Category.objects.filter(parent=None, published=True)
	town = Town.objects.get(slug=slug)
	towns = Town.objects.exclude(id=town.id).exclude(main_page=True)
	gallery = None

	try:
		main_page_town = Town.objects.get(main_page=True)
		gallery = Gallery.objects.get(category__slug=town.slug)

	except Exception, e:
		pass

	hotels = PointOfInterest.objects.filter(town=town, point_type=3)
	restaurants = PointOfInterest.objects.filter(town=town, point_type=2)
	places = PointOfInterest.objects.filter(town=town, point_type=1)

	articles = Article.objects.filter(category__slug=town.slug)

	return render_to_response('vive_boyaca/town.html', 
		{'gallery':gallery,'categories':categories, 
		 'main_town':main_page_town, 'towns':towns, 
		 'town':town, 'hotels':hotels, 'places':places, 'restaurants':restaurants,
		 'articles': articles,
		})

from django.db.models import Q
def vive_boyaca_home(request):
	categories = Category.objects.filter(parent=None, published=True)
	poll = None
	main_page_town = None
	gallery = None

	try:
		main_page_town = Town.objects.get(main_page=True)
		gallery = Gallery.objects.get(category__slug=main_page_town.slug)
	except Exception, e:
		pass
	
	category = get_object_or_404(Category, slug='vive-boyaca')
	articles = Article.objects.filter(
    	Q(category=category) | Q(category__parent=category)
    )
    
	towns = Town.objects.exclude(id=main_page_town.id)

	try:
		poll = Poll.objects.get(closed=False)
	except Exception as e:
		pass

	return render_to_response('vive_boyaca/home.html', 
		{'towns':towns,'main_town':main_page_town, 'articles':articles, 'categories':categories, 'poll':poll, 'gallery':gallery}
	)

