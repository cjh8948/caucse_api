from django.conf.urls.defaults import patterns

urlpatterns = patterns('apiprj.api1_app.views',
    (r'^articles/create', 'articles_create'),                       
    (r'^articles/list', 'articles_list'),
    (r'^articles/show', 'articles_show'),
    (r'^comments/create', 'comments_create'),
    (r'^users/show', 'users_show'),
    (r'^users/lookup', 'users_lookup'),
    (r'^boards/lookup', 'boards_lookup'),
    (r'^$', 'index')
)
