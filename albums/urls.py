from django.conf.urls import patterns, include, url

urlpatterns = patterns('albums.views',
    #url(r'^$', 'index'),
    url(r'^$', 'index'),
    url(r'^(?P<year>\d{4})/$', 'year'),
    url(r'^(?P<year>\d{4})/(?P<event>\w+)/$', 'event'),
)
