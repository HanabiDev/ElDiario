from django.shortcuts import render_to_response
from django.template import RequestContext
from content.models import Article
# Create your views here.

TEMPLATE_DIR = 'frontend/../'
def home(request):

	full_width_article = None
	try:
		full_width_article = Article.objects.get(full_width=True)
	except Exception, e:
		pass

	all_articles = Article.objects.exclude(full_width=True).order_by('-creation_date')
	
	return render_to_response(TEMPLATE_DIR+'site_index.html', 
		{'full_width_article': full_width_article, 'articles':all_articles}, 
		context_instance=RequestContext(request)
	)

def serve_article(request, slug):
	article = Article.objects.get(slug=slug)

	print article

	return render_to_response(TEMPLATE_DIR+'article.html', {'article':article})