from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^', include('frontend.urls')),
    url(r'^backend', include('admin.urls')),
    url(r'^mobile', include('mobile.urls')),
    url(r'^redactor/', include('redactor.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'session_security/', include('session_security.urls')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)