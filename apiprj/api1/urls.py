from django.conf.urls.defaults import *

urlpatterns = patterns('api1.views',
    (r'^articles/list', 'articles_list'),
    (r'^articles/show', 'articles_show'),
    (r'^users/show', 'users_show'),
    (r'^users/lookup', 'users_lookup'),
    (r'^boards/lookup', 'boards_lookup'),
)
