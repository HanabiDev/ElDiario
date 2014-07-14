from django.conf.urls import patterns, url, include

urlpatterns = patterns('',

    url(r'^/$', 'polls.views.list_polls', name='polls'),
    url(r'^/nueva/', 'polls.views.add_poll', name='new_poll'),
  	url(r'^/editar/(?P<id>\d+)/$', 'polls.views.edit_poll', name='edit_poll'),
	  url(r'^/publicar/(?P<id>\d+)/$', 'polls.views.toggle_publish', name='toggle_publish'),
	  url(r'^/despublicar/(?P<id>\d+)/$', 'polls.views.toggle_publish', name='toggle_publish'),
	  url(r'^/eliminar/$', 'polls.views.delete_poll', name='delete_poll'),
)
