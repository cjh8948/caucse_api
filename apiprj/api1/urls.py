from django.conf.urls.defaults import *

urlpatterns = patterns('api1.views',
    (r'^users/show', 'users_show'),
    (r'^users/lookup', 'users_lookup'),
    (r'^boards/lookup', 'boards_lookup'),
)
