from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # index
    (r'^$', 'apiprj.api1_app.views.index'),
    # accounts
    (r'^accounts/$', 'apiprj.api1_app.views.index'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    # consumer
    (r'^consumer/show/(?P<consumer_key>.+)',
     'apiprj.oauth_app.views.consumer_show'),
    # oauth
    (r'^oauth/', include('apiprj.oauth_app.urls')),
    # api
    (r'^1/', include('apiprj.api1_app.urls')),
    (r'^', include('apiprj.api1_app.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                   (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                    {'document_root':settings.STATIC_DOC_ROOT}))
