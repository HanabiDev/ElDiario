from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$', 'ads.views.home', name='home'),
    url(r'^/nueva/', 'ads.views.add_ad', name='new_add'),
	url(r'^/editar/(?P<id>\d+)/$', 'ads.views.edit_ad', name='edit_ad'),
	url(r'^/publicar/$', 'ads.views.publish_group', name='publish_group'),
	url(r'^/despublicar/$', 'ads.views.unpublish_group', name='unpublish_group'),
	url(r'^/publicar/(?P<id>\d+)/$', 'ads.views.toggle_publish', name='toggle_publish'),
	url(r'^/despublicar/(?P<id>\d+)/$', 'ads.views.toggle_publish', name='toggle_publish'),
	url(r'^/eliminar/$', 'ads.views.delete_ad', name='delete_ad'),
)