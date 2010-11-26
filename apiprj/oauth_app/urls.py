from django.conf.urls.defaults import patterns

urlpatterns = patterns('oauth_app.views',
    (r'^request_token', 'request_token'),
    (r'^access_token', 'access_token'),
    (r'^authorize', 'authorize'),
)
