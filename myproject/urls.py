from django.conf.urls import patterns, include, url
from django.contrib import admin

from web_portal.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name='index'),
)
