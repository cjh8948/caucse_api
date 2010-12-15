from django.conf.urls.defaults import patterns

urlpatterns = patterns('apiprj.api1_app.views',
    (r'^articles/create/(?P<board_id>(board|photo)_.+)', 'articles_create'),
    (r'^articles/create', 'articles_create'),
    (r'^articles/list/(?P<board_id>(board|photo)_.+)', 'articles_list'),
    (r'^articles/list', 'articles_list'),
    (r'^articles/show/(?P<board_id>(board|photo)_.+)/(?P<article_id>\d+)', 'articles_show'),
    (r'^articles/show', 'articles_show'),
    (r'^boards/favorite', 'boards_favorite'),
    (r'^boards/lookup', 'boards_lookup'),
    (r'^comments/create/(?P<board_id>(board|photo)_.+)/(?P<article_id>\d+)', 'comments_create'),
    (r'^comments/create', 'comments_create'),
    (r'^favorites/list', 'favorites_list'),
    (r'^users/show/(?P<user_id>.+)', 'users_show'),
    (r'^users/show', 'users_show'),
    (r'^users/lookup', 'users_lookup'),
    (r'^users/search', 'users_search'),
    
    (r'^consumer/show/(?P<consumer_key>.+)', 'consumer_show'),
)
