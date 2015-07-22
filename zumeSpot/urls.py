from django.conf.urls import patterns, include, url
from django.contrib import admin

from zumeSpot import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zumeSpot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'zFeed.views.home', name='home'),
    url(r'^getHomePosts/', 'zFeed.views.getHomePosts', name='getHomePosts'),
    url(r'^getVenuePosts/', 'zFeed.views.getVenuePosts', name='getVenuePosts'),
    url(r'^menWith/', 'zFeed.views.menWith', name='menWith'),
)
