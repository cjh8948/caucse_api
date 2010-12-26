from django.conf.urls.defaults import patterns

urlpatterns = patterns('apiprj.api1_app.views',
    # json resources
    (r'^articles/create/(?P<board_id>(board|photo)_.+)', 'articles_create'),
    (r'^articles/create', 'articles_create'),
    (r'^articles/delete/(?P<board_id>(board|photo)_.+)/(?P<article_id>\d+)', 'articles_delete'),
    (r'^articles/delete', 'articles_delete'),
    (r'^articles/list/(?P<board_id>(board|photo)_.+)', 'articles_list'),
    (r'^articles/list', 'articles_list'),
    (r'^articles/show/(?P<board_id>(board|photo)_.+)/(?P<article_id>\d+)', 'articles_show'),
    (r'^articles/show', 'articles_show'),
    (r'^articles/update/(?P<board_id>(board|photo)_.+)/(?P<article_id>\d+)', 'articles_update'),
    (r'^articles/update', 'articles_update'),
    (r'^boards/favorite', 'boards_favorite'),
    (r'^boards/lookup', 'boards_lookup'),
    (r'^comments/create/(?P<board_id>(board|photo)_.+)/(?P<article_id>\d+)', 'comments_create'),
    (r'^comments/create', 'comments_create'),
    (r'^comments/delete/(?P<board_id>(board|photo)_.+)/(?P<comment_id>\d+)', 'comments_delete'),
    (r'^comments/delete', 'comments_delete'),
    (r'^favorites/list', 'favorites_list'),
    (r'^users/show/(?P<user_id>.+)', 'users_show'),
    (r'^users/show', 'users_show'),
    (r'^users/lookup', 'users_lookup'),
    (r'^users/search', 'users_search'),

    # html pages
    (r'^apireference', 'apireference'),
    (r'^myapp', 'myapp'),
    (r'^apistatus', 'apistatus'),
    (r'^$', 'index'),
)
