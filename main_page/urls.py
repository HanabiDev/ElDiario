from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^/$', 'main_page.views.load_manager', name='mainpage_manager'),
)
