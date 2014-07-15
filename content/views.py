#encoding: utf-8
from django.shortcuts import render_to_response, HttpResponseRedirect, redirect
from django.template import RequestContext
from models import *
from forms import *
from django.contrib.auth.decorators import permission_required, login_required
# Create your views here.

TEMPLATE_DIR = 'content/../'

def home(request):
	return redirect('/backend')

"""
------------------------------------------------------------------------------------
Category views
------------------------------------------------------------------------------------
"""

@login_required(login_url='login')
def list_categories(request):
	categories = Category.objects.all()


	for category in categories:



		articles = category.article_set.all().count()
		category.articles = articles
		category.subcats = category.parent_cat.all().count()

	return render_to_response(TEMPLATE_DIR+'categories/index.html', {'cat_list':categories},
							   context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('content.add_category', login_url='/backend/permisos_insuficientes/')
def add_category(request):

	if request.method == 'GET':
		form = CategoryForm()
		return render_to_response(TEMPLATE_DIR+'categories/add_edit.html',
							  {'form':form}, context_instance=RequestContext(request))

	elif request.method == 'POST':
		form = CategoryForm(request.POST)
        if form.is_valid():
					new_category = form.save()
					category_pos = new_category.main_page_position

					Category.objects.filter(main_page_position=new_category.main_page_position).update(main_page_position=None)

					new_category.main_page_position = category_pos
					new_category.save()

					return HttpResponseRedirect('/backend/contenido/categorias')
        else:
        	return render_to_response(TEMPLATE_DIR+'categories/add_edit.html',
							  {'form':form}, context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('content.change_category', login_url='/backend/permisos_insuficientes/')
def edit_category(request, id):

	category = Category.objects.get(id=id)

	if request.method == 'GET':
		form = CategoryForm(instance=category)
		return render_to_response(TEMPLATE_DIR+'categories/add_edit.html',
		{'form':form, 'editing':True, 'title':category.title}, context_instance=RequestContext(request))

	elif request.method == 'POST':
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			new_category = form.save()
			category_pos = new_category.main_page_position

			Category.objects.filter(main_page_position=new_category.main_page_position).update(main_page_position=None)

			new_category.main_page_position = category_pos
			new_category.save()
			return HttpResponseRedirect('/backend/contenido/categorias')
		else:
			return render_to_response(TEMPLATE_DIR+'categories/add_edit.html',
			{'form':form, 'editing':True, 'title':category.title}, context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('content.change_category', login_url='/backend/permisos_insuficientes/')
def publish_group(request):
	ids = request.POST.getlist('id')
	for cat_id in ids:
		category = Category.objects.get(id=int(cat_id))
		category.published = True
		category.save()
	return HttpResponseRedirect('/backend/contenido/categorias')

@login_required(login_url='login')
@permission_required('content.change_category', login_url='/backend/permisos_insuficientes/')
def unpublish_group(request):
	ids = request.POST.getlist('id')
	for cat_id in ids:
		category = Category.objects.get(id=int(cat_id))
		category.published = False
		category.save()
	return HttpResponseRedirect('/backend/contenido/categorias')

@login_required(login_url='login')
@permission_required('content.change_category', login_url='/backend/permisos_insuficientes/')
def toggle_publish(request, id):
	category = Category.objects.get(id=id)
	category.published = not category.published
	category.save()
	return HttpResponseRedirect('/backend/contenido/categorias')

@login_required(login_url='login')
@permission_required('content.delete_category', login_url='/backend/permisos_insuficientes/')
def delete_category(request):
	ids = request.POST.getlist('id')
	for cat_id in ids:
		category = Category.objects.get(id=int(cat_id))
		category.delete()
	return HttpResponseRedirect('/backend/contenido/categorias')


"""
------------------------------------------------------------------------------------
Article views
------------------------------------------------------------------------------------
"""

@login_required(login_url='login')
def list_articles(request, message=None):
	articles = Article.objects.all()
	return render_to_response(TEMPLATE_DIR+'articles/index.html', {'art_list':articles},
							   context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('content.add_article', login_url='/backend/permisos_insuficientes/')
def add_article(request):

	if request.method == 'GET':
		form = ArticleForm()
		return render_to_response(TEMPLATE_DIR+'articles/add_edit.html',
							  {'form':form}, context_instance=RequestContext(request))

	elif request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			new_article = form.save()
			if not request.user.is_superuser:
				new_article.published = False
				new_article.save()

			if new_article.full_width:
				Article.objects.filter(full_width=True).exclude(id=new_article.id).update(full_width=False)

			return HttpResponseRedirect('/backend/contenido/articulos/')
		else:
			return render_to_response(TEMPLATE_DIR+'articles/add_edit.html',
						{'form':form}, context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('content.change_article', login_url='/backend/permisos_insuficientes/')
def edit_article(request, id):

	article = Article.objects.get(id=id)

	if request.method == 'GET':
		form = ArticleForm(instance=article)
		return render_to_response(TEMPLATE_DIR+'articles/add_edit.html',
							  {'form':form, 'editing':True, 'title':article.title}, context_instance=RequestContext(request))

	elif request.method == 'POST':
		form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            new_article = form.save()

            if new_article.full_width:
				Article.objects.filter(full_width=True).exclude(id=new_article.id).update(full_width=False)

            return HttpResponseRedirect('/backend/contenido/articulos')
        else:
        	return render_to_response(TEMPLATE_DIR+'articles/add_edit.html',
							  {'form':form, 'editing':True, 'title':article.title}, context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('content.change_article', login_url='/backend/permisos_insuficientes/')
def publish_art_group(request):
	ids = request.POST.getlist('id')
	for art_id in ids:
		article = Article.objects.get(id=int(art_id))
		article.published = True
		article.save()
	return HttpResponseRedirect('/backend/contenido/articulos')

@login_required(login_url='login')
@permission_required('content.change_article', login_url='/backend/permisos_insuficientes/')
def unpublish_art_group(request):
	ids = request.POST.getlist('id')
	for art_id in ids:
		article = Article.objects.get(id=int(art_id))
		article.published = False
		article.save()
	return HttpResponseRedirect('/backend/contenido/articulos')

@login_required(login_url='login')
@permission_required('content.change_article', login_url='/backend/permisos_insuficientes/')
def toggle_art_publish(request, id):
	article = Article.objects.get(id=id)
	article.published = not article.published
	article.save()
	return HttpResponseRedirect('/backend/contenido/articulos')


@login_required(login_url='login')
@permission_required('content.change_article', login_url='/backend/permisos_insuficientes/')
def feature_art_group(request):
	ids = request.POST.getlist('id')
	for art_id in ids:
		article = Article.objects.get(id=int(art_id))
		article.featured = True
		article.save()
	return HttpResponseRedirect('/backend/contenido/articulos')

@login_required(login_url='login')
@permission_required('content.change_article', login_url='/backend/permisos_insuficientes/')
def unfeature_art_group(request):
	ids = request.POST.getlist('id')
	for art_id in ids:
		article = Article.objects.get(id=int(art_id))
		article.featured = False
		article.save()
	return HttpResponseRedirect('/backend/contenido/articulos')

@login_required(login_url='login')
@permission_required('content.change_article', login_url='/backend/permisos_insuficientes/')
def toggle_art_featured(request, id):
	article = Article.objects.get(id=id)
	article.featured = not article.featured
	article.save()
	return HttpResponseRedirect('/backend/contenido/articulos')


@login_required(login_url='login')
@permission_required('content.delete_article', login_url='/backend/permisos_insuficientes/')
def delete_article(request):
	ids = request.POST.getlist('id')
	for art_id in ids:
		article = Article.objects.get(id=int(art_id))
		article.delete()
	return HttpResponseRedirect('/backend/contenido/articulos')
