from django.conf.urls.defaults import patterns, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/$', 'apiprj.api1_app.views.index'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^oauth/', include('apiprj.oauth_app.urls')),
    (r'^1/', include('apiprj.api1_app.urls')),
    (r'^$', 'apiprj.api1_app.views.index'),
    (r'^', include('apiprj.api1_app.urls')),
)