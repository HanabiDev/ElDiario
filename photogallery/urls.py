from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^/$', 'photogallery.views.home', name='home'),
    url(r'^/nueva/', 'photogallery.views.add_gallery', name='new_gallery'),
	url(r'^/editar/(?P<id>\d+)/$', 'photogallery.views.edit_gallery', name='edit_gallery'),
	url(r'^/publicar/$', 'photogallery.views.publish_group', name='publish_group'),
	url(r'^/despublicar/$', 'photogallery.views.unpublish_group', name='unpublish_group'),
	url(r'^/publicar/(?P<id>\d+)/$', 'photogallery.views.toggle_publish', name='toggle_publish'),
	url(r'^/despublicar/(?P<id>\d+)/$', 'photogallery.views.toggle_publish', name='toggle_publish'),
	url(r'^/eliminar/$', 'photogallery.views.delete_gallery', name='delete_gallery'),
	url(r'^/upload/$', 'photogallery.views.upload'),
	url(r'^/get_preview/$', 'photogallery.views.get_preview'),
	url(r'^/edit_image/(?P<id>\d+)/$', 'photogallery.views.edit_image'),
	url(r'^/imagenes/$', 'photogallery.views.index_images'),
	url(r'^/imagenes/nueva/$', 'photogallery.views.new_image'),
	url(r'^/imagenes/editar/(?P<id>\d+)/$', 'photogallery.views.edit_image'),
	url(r'^/imagenes/eliminar/$', 'photogallery.views.delete_image'), 
)
