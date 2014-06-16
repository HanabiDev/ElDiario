from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$', 'content.views.home', name='home'),
    
    url(r'^/categorias/$', 'content.views.list_categories', name='categories'),
    url(r'^/categorias/nueva/', 'content.views.add_category', name='new_category'),
	url(r'^/categorias/editar/(?P<id>\d+)/$', 'content.views.edit_category', name='edit_category'),
	url(r'^/categorias/publicar/$', 'content.views.publish_group', name='publish_group'),
	url(r'^/categorias/despublicar/$', 'content.views.unpublish_group', name='unpublish_group'),
	url(r'^/categorias/publicar/(?P<id>\d+)/$', 'content.views.toggle_publish', name='toggle_publish'),
	url(r'^/categorias/despublicar/(?P<id>\d+)/$', 'content.views.toggle_publish', name='toggle_publish'),
	url(r'^/categorias/eliminar/$', 'content.views.delete_category', name='delete_category'),
    
    url(r'^/articulos/$', 'content.views.list_articles', name='articles'),
    url(r'^/articulos/nuevo/', 'content.views.add_article', name='new_article'),
    url(r'^/articulos/editar/(?P<id>\d+)/$', 'content.views.edit_article', name='edit_article'),
    url(r'^/articulos/publicar/$', 'content.views.publish_art_group', name='publish_art_group'),
	url(r'^/articulos/despublicar/$', 'content.views.unpublish_art_group', name='unpublish_art_group'),
	url(r'^/articulos/destacar/$', 'content.views.feature_art_group', name='publish_art_group'),
	url(r'^/articulos/no_destacar/$', 'content.views.unfeature_art_group', name='unpublish_art_group'),
	url(r'^/articulos/publicar/(?P<id>\d+)/$', 'content.views.toggle_art_publish', name='toggle_art_publish'),
	url(r'^/articulos/despublicar/(?P<id>\d+)/$', 'content.views.toggle_art_publish', name='toggle_art_publish'),
	url(r'^/articulos/destacar/(?P<id>\d+)/$', 'content.views.toggle_art_featured', name='toggle_art_publish'),
	url(r'^/articulos/no_destacar/(?P<id>\d+)/$', 'content.views.toggle_art_featured', name='toggle_art_publish'),
	url(r'^/articulos/eliminar/$', 'content.views.delete_article', name='delete_article'),
)