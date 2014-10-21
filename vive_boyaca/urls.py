from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$', 'vive_boyaca.views.list_towns', name='home'),
    url(r'^/nuevo/', 'vive_boyaca.views.add_town', name='new_town'),
  	url(r'^/editar/(?P<id>\d+)/$', 'vive_boyaca.views.edit_town', name='edit_town'),
  	url(r'^/publicar/$', 'vive_boyaca.views.publish_group', name='toggle_publish'),
  	url(r'^/publicar/(?P<id>\d+)/$', 'vive_boyaca.views.toggle_publish', name='toggle_publish'),
  	url(r'^/despublicar/$', 'vive_boyaca.views.unpublish_group', name='toggle_publish'),
  	url(r'^/despublicar/(?P<id>\d+)/$', 'vive_boyaca.views.toggle_publish', name='toggle_publish'),
  	url(r'^/eliminar/$', 'vive_boyaca.views.delete_town', name='delete_town'),
  	url(r'^/poi/$', 'vive_boyaca.views.poi_home', name='poi_home'),
  	url(r'^/poi/nuevo/$', 'vive_boyaca.views.add_poi', name='add_poi'),
  	url(r'^/poi/editar/(?P<id>\d+)/$', 'vive_boyaca.views.edit_poi', name='edit_poi'),
  	url(r'^/poi/eliminar/$', 'vive_boyaca.views.delete_poi', name='delete_poi'),

)