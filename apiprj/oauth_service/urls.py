from django.conf.urls.defaults import *

urlpatterns = patterns('oauth_service.views',
    (r'^request_token', 'request_token'),
)
