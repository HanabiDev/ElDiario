from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^$', 'frontend.views.home', name='site_home'),
	url(r'^articulos/$', 'frontend.views.all_articles', name='all_articles'),
	url(r'^articulos/(?P<slug>[-\w]+)/$', 'frontend.views.serve_article', name='serve_article'),
	url(r'^categorias/(?P<slug>[-\w]+)/$', 'frontend.views.serve_category', name='serve_category'),
	url(r'^categorias/$', 'frontend.views.all_cats', name='all_cats'),
	url(r'^fotogalerias/(?P<slug>[-\w]+)/$', 'frontend.views.serve_gallery', name='serve_gallery'),
	url(r'^encuestas/votar/$', 'polls.views.vote', name='vote'),
	url(r'^encuestas/resultados/(?P<id>[-\d]+)/$', 'polls.views.get_results', name='get_results'),
	url(r'^suscribirse/$', 'suscriptions.views.frontend_suscription', name='frontend_suscription'),
	url(r'^ediciones_impresas/$', 'frontend.views.impressed', name='impressed'),
)
