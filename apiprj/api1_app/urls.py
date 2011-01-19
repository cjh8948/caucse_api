from django.conf.urls.defaults import patterns

urlpatterns = patterns('apiprj.api1_app.views',
    # json resources
    (r'^articles/create/(?P<board_id>.+)', 'articles_create'),
    (r'^articles/delete/(?P<board_id>.+)/(?P<article_id>\d+)', 'articles_delete'),
    (r'^articles/list/(?P<board_id>.+)', 'articles_list'),
    (r'^articles/show/(?P<board_id>.+)/(?P<article_id>\d+)', 'articles_show'),
    (r'^articles/update/(?P<board_id>.+)/(?P<article_id>\d+)', 'articles_update'),
    (r'^boards/favorite', 'boards_favorite'),
    (r'^boards/lookup', 'boards_lookup'),
    (r'^comments/create/(?P<board_id>.+)/(?P<article_id>\d+)', 'comments_create'),
    (r'^comments/delete/(?P<board_id>.+)/(?P<comment_id>\d+)', 'comments_delete'),
    (r'^favorites/list', 'favorites_list'),
    (r'^users/show/(?P<user_id>.+)', 'users_show'),
    (r'^users/show', 'users_show'),
    (r'^users/lookup', 'users_lookup'),
    (r'^users/search', 'users_search')
)
