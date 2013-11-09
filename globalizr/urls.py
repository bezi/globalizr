# Routing logic for API and html
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Homepage
    url(r'^$', 'globalizr.views.home'),
    url(r'^home/$', 'globalizr.views.home'),
    # About page
    url(r'^about/$', 'globalizr.views.about'),

    # World page: Debugging information.
    url(r'^world/$', 'globalizr.views.world'),

    # API
    #-- query
    url(r'^api/query/(\w+)/$', 'globalizr.api.views.query'),
    
    #-- interface
    url(r'^api/interface/(\w+)/(\w+)/$', 'globalizr.api.views.interface')
)
