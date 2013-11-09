from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'globalizr.views.home', name='home'),
    url(r'^home/$', 'globalizr.views.home', name='home'),
    url(r'^about/$', 'globalizr.views.about', name='about'),
    url(r'^query/?P<query>[A-Za-z0-9-]+/$', 'globalizr.views.query', name='query'),
)
