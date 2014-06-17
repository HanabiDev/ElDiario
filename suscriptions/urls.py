from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$', 'suscriptions.views.list_suscriptions', name='suscriptions'),
    url(r'^/nueva/', 'suscriptions.views.add_suscription', name='new_suscription'),
    url(r'^/editar/(?P<id>\d+)/$', 'suscriptions.views.edit_suscription', name='edit_suscription'),
    url(r'^/activar/$', 'suscriptions.views.activate_group', name='activate_group'),
    url(r'^/desactivar/$', 'suscriptions.views.deactivate_group', name='deactivate_group'),
    url(r'^/activar/(?P<id>\d+)/$', 'suscriptions.views.toggle_publish', name='toggle_publish'),
    url(r'^/desactivar/(?P<id>\d+)/$', 'suscriptions.views.toggle_publish', name='toggle_publish'),
    url(r'^/eliminar/$', 'suscriptions.views.delete_suscription', name='delete_category'),
)