from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$', 'admin.views.home', name='home'),
	url(r'^/login', 'admin.views.admin_login', name='login'),
	url(r'^/logout', 'admin.views.admin_logout', name='logout'),
	url(r'^/permisos_insuficientes/', 'admin.views.no_perms', name='no_perms'),
	url(r'^/nuevo_password', 'admin.views.set_new_password', name='new_password'),
    url(r'^/contenido', include('content.urls')),
    url(r'^/fotogalerias', include('photogallery.urls')),
    url(r'^/publicidad', include('ads.urls')),
    url(r'^/acceso', include('auth.urls')),
    url(r'^/encuestas', include('polls.urls')),
)