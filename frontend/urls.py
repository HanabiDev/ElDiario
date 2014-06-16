from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^$', 'frontend.views.home', name='site_home'),
	url(r'^articulos/(?P<slug>[-\w]+)/$', 'frontend.views.serve_article', name='serve_article'),
)