from django.conf.urls.defaults import patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^apitest/', include('apitest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^oauth/', include('apiprj.oauth_app.urls')),
    (r'^1/', include('apiprj.api1_app.urls')),
    (r'^', include('apiprj.api1_app.urls')),
)
