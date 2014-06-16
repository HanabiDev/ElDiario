from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$', 'auth.views.home', name='home'),
	url(r'^/(?P<view>\w+)/$', 'auth.views.home', name='home_users'),

	url(r'^/usuarios/nuevo/$', 'auth.views.add_user', name='add_user'),
	url(r'^/usuarios/editar/(?P<id>\d+)/$', 'auth.views.edit_user', name='edit_user'),
	url(r'^/usuarios/editar/(?P<id>\d+)/cambiar_password/$', 'auth.views.change_pass', name='new_password'),
	url(r'^/usuarios/bloquear/$', 'auth.views.toggle_lock_group', name='toggle_lock_group'),
	url(r'^/usuarios/desbloquear/$', 'auth.views.toggle_unlock_group', name='toggle_unlock_group'),
	url(r'^/usuarios/bloquear/(?P<id>\d+)$', 'auth.views.toggle_lock', name='toggle_lock'),
	url(r'^/usuarios/desbloquear/(?P<id>\d+)$', 'auth.views.toggle_lock', name='toggle_lock'),

	url(r'^/grupos/nuevo/$', 'auth.views.add_group', name='add_user'),
	url(r'^/grupos/editar/(?P<id>\d+)/$', 'auth.views.edit_group', name='edit_user'),
	url(r'^/grupos/eliminar/$', 'auth.views.delete_group', name='toggle_lock'),
)