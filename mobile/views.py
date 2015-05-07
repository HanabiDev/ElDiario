from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from content.models import *
from ads.models import Ad
from django.db.models import Q

TEMPLATE_DIR = 'mobile/../'
# Create your views here.
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

	gallery = None
	carousel_images = None
	order = None
	try:
		gallery = Gallery.objects.filter(published=True).order_by('-creation_date')[0]
		carousel_images = gallery.images.all()
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

	try:
		count = Article.objects.filter(full_width=False, published=True).exclude(category__title='Caricaturas').count()
		if count > 0:
			main_art = Article.objects.filter(
				full_width=False,
				published=True
			).exclude(category__title='Caricaturas').order_by('-creation_date')[0]

			all_articles = Article.objects.filter(
				full_width=False, published=True
			).exclude(category__title='Caricaturas').order_by('-creation_date')[1:20]

	except Exception as e:
		pass

	return render_to_response(TEMPLATE_DIR+'mobile_index.html',
		{'full_width_article': full_width_article,
		'poll':poll, 'articles':all_articles,
		'categories': categories, 'main_art':main_art,
		'images':carousel_images, 'gallery':gallery, 'order':order,
		'cartoons':cartoons, 'orderCartoons':orderCartoons
		},
		context_instance=RequestContext(request)
		)

def all_articles(request):

	articles = Article.objects.filter(published=True).order_by('-creation_date')
	categories = Category.objects.filter(parent=None, published=True)

	return render_to_response(TEMPLATE_DIR+'mobile_category.html', {'articles':articles, 'all_arts':True, 'categories':categories})

def serve_article(request, slug):
	article = get_object_or_404(Article, slug=slug)
	article.hits = article.hits + 1
	article.save()
	categories = Category.objects.filter(parent=None, published=True)

	return render_to_response(TEMPLATE_DIR+'mobile_article.html', {'article':article, 'categories':categories})

def serve_category(request, slug):
	if slug == "general":
		category = None
	else:
		category = get_object_or_404(Category, slug=slug)

	articles = Article.objects.filter(category=category).order_by('-creation_date')
	categories = Category.objects.filter(parent=None, published=True)

	return render_to_response(TEMPLATE_DIR+'mobile_category.html', {'articles':articles, 'category':category, 'categories':categories})

def all_cats(request):
	categories = Category.objects.filter(parent=None, published=True)
	return render_to_response(TEMPLATE_DIR+'mobile_categories.html', {'all_arts':True, 'categories':categories})

def search(request):

	keyword = request.GET.get('keyword')

	if keyword:
		categories = Category.objects.filter(
			Q(title__contains=keyword) | Q(description__contains=keyword)
		).exclude(published=False)

		articles = Article.objects.filter(
			Q(title__contains=keyword) | Q(abstract__contains=keyword) | Q(content__contains=keyword)
		).exclude(published=False)

		m_categories = Category.objects.filter(parent=None, published=True)

		return render_to_response(TEMPLATE_DIR+'mobile_search.html', {'keyword':keyword, 'articles':articles, 'categories':categories, 'menu':m_categories})
	else:
		return redirect('/')
