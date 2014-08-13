from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = patterns('',
	url(r'^$', 'mobile.views.home', name='mobile_home'),
	url(r'^articulos/$', 'mobile.views.all_articles', name='all_articles'),
	url(r'^articulos/(?P<slug>[-\w]+)/$', 'mobile.views.serve_article', name='serve_article'),
	url(r'^categorias/(?P<slug>[-\w]+)/$', 'mobile.views.serve_category', name='serve_category'),
	url(r'^categorias/$', 'mobile.views.all_cats', name='all_cats'),
	url(r'^buscar/$', 'mobile.views.search', name='search'),
)