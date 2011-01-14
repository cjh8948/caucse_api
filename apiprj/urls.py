from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # accounts
    (r'^accounts/$', 'apiprj.api1_app.views.index'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^accounts/logout_then_login/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^accounts/profile/$', 'apiprj.api1_app.views.myapp'),
    # admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    # oauth
    (r'^oauth/', include('apiprj.oauth_app.urls')),
    # api
    (r'^1/', include('apiprj.api1_app.urls')),
    (r'^', include('apiprj.api1_app.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                   (r'^api_static/(?P<path>.*)$', 'django.views.static.serve',
                    {'document_root':settings.STATIC_DOC_ROOT}))
