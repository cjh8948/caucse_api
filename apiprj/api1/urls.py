from django.conf.urls.defaults import *

urlpatterns = patterns('api1',
    (r'^users/show', 'users.show'),
    (r'^users/lookup', 'users.lookup'),
)
