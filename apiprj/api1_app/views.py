from django.http import HttpResponse
from django.utils.simplejson import dumps
from django.views.decorators.csrf import csrf_exempt
from apiprj.oauth_app.utils.decorators import oauth_required
from modelwrap import Article, Board, Comment, User, Token

@oauth_required
def articles_show(request):
    """This API returns array of articles
    
    resource: 'articles/show'
    method: GET, oauth required, rate limited
    mandatory parameter: board_id, article_id"""
    board_id = request.GET['board_id']
    article_id = int(request.GET['article_id'])
    article = Article.get(board_id, article_id)
    ret = dumps(article, ensure_ascii=False) 
    return HttpResponse(ret)
    
@oauth_required
def users_show(request):
    """This API returns user
    
    resource: 'users/show'
    method: GET, oauth required, rate limited
    mandatory parameter: user_id"""
    id = request.GET['user_id']
    user = User.get(id)
    ret = dumps(user, ensure_ascii=False)
    return HttpResponse(ret)
    
@oauth_required
def users_lookup(request):
    """This API returns array of users
    
    resource: 'users/lookup'
    method: GET, oauth required, rate limited
    mandatory parameter: user_id (comma separated)"""
    id_list = request.GET['user_id'].split(',')
    users = map(User.get, id_list)
    ret = dumps(users, ensure_ascii=False)
    return HttpResponse(ret)
 
def boards_lookup(request):
    """This API returns array of boards
    
    resource: 'boards/lookup'
    method: GET, oauth not required, rate limited
    mandatory parameter: board_id (comma separated)"""
    board_list = request.GET['board_id'].split(',')
    boards = map(Board.get, board_list)
    ret = dumps(boards, ensure_ascii=False)
    return HttpResponse(ret)

@oauth_required
def articles_list(request):
    """This API returns array of articles and list option. 
    
    resource: 'articles/list'
    method: GET, oauth required, rate limited
    mandatory parameter: board_id
    optional parameter: page(default=0), per_page(default=20)"""
    page = 0
    per_page = 20
    
    # get request parameter
    try: 
        board_id = request.GET['board_id']
    except KeyError as e:
        ret = dumps({'status':'error', 'message':e.message})
        return HttpResponse(ret)

    if request.GET.has_key('page'):
        page = int(request.GET['page'])
    if request.GET.has_key('per_page'):
        per_page = int(request.GET['per_page'])

    # make json object to return
    articles = Article.get_list(board_id, page, per_page)
    ret_item = {'option': {'board_id': board_id,
                           'page': page,
                           'per_page': per_page},
                'articles': articles}
    ret = dumps(ret_item, ensure_ascii=False)

    return HttpResponse(ret)

@csrf_exempt
@oauth_required
def comments_update(request):
    """This API posts a comment. 
    
    resource: 'comments/update'
    method: POST, oauth required, rate limited
    mandatory parameter: board_id, article_id, message"""
    # read parameter
    try:
        board_id = request.POST['board_id']
        article_id = request.POST['article_id']
        message = request.POST['message']
        oauth_token = request.POST['oauth_token']
    except KeyError as e:
        ret = dumps({'status':'error', 'message':e.message})
        return HttpResponse(ret)
    
    # update comment
    try:
        user_id = Token.get_user_id(oauth_token)
        Comment.post(board_id=board_id, article_id=article_id,
                               user_id=user_id, content=message)
    except Exception as e:
        ret = dumps({'status':'error', 'message':e.message})
        return HttpResponse(ret)
    
    # return result
    ret = dumps({'status':'ok'})    
    return HttpResponse(ret)
