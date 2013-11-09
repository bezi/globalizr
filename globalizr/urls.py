from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'globalizr.views.home', name='home'),
    url(r'^home/$', 'globalizr.views.home', name='home'),
    url(r'^about/$', 'globalizr.views.about', name='about'),
    url(r'^query/$', 'globalizr.views.query', name='query'),
    url(r'^query/(\w+)/$', 'globalizr.views.query', name='query'),
)
