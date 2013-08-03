from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url('', include('fotis.albums.urls')),
    url('^admin/', include(admin.site.urls)),
)
