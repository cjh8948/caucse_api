#! -*- coding: utf8 -*- 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.simplejson import dumps
from django.views.decorators.csrf import csrf_exempt
from apiprj.oauth_app.models import Consumer
from apiprj.oauth_app.utils.decorators import oauth_required
from modelwrap import Article, Board, Comment, User, Token, Favorite, Cafe

@csrf_exempt
@oauth_required
def articles_create(request, board_id=None):
    """This API posts an article.
    
    * resource: 'articles/create'
    ** method: POST, oauth required, rate limited
    ** mandatory parameter: board_id, title, message"""
    try:
        if not board_id:
            board_id = request.POST['board_id']
        title = request.POST['title']
        message = request.POST['message']
        oauth_token = request.POST['oauth_token']
    except KeyError as e:
        ret = dumps({'status':'error', 'message':e.message})
        return HttpResponse(ret)
    
    user_id = Token.get_user_id(oauth_token)
    Article.post(board_id=board_id, user_id=user_id, title=title,
                 message=message)

    # return result
    ret = dumps({'status':'ok'})    
    return HttpResponse(ret)

@oauth_required
def articles_list(request, board_id=None):
    """This API returns array of articles and list option. 
    
    * resource: 'articles/list'
    ** method: GET, oauth required, rate limited
    ** mandatory parameter: board_id
    ** optional parameter: page(default=0), per_page(default=20)"""
    page = 0
    per_page = 20
    
    # get request parameter
    try: 
        if not board_id:
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
    ret = dumps(ret_item)

    return HttpResponse(ret)

@oauth_required
def articles_show(request, board_id=None, article_id=None):
    """This API returns array of articles
    
    * resource: 'articles/show'
    ** method: GET, oauth required, rate limited
    ** mandatory parameter: board_id, article_id"""
    if not board_id:
        board_id = request.GET['board_id']
    if not article_id:
        article_id = int(request.GET['article_id'])
    article = Article.get(board_id, article_id)
    ret = dumps(article) 
    return HttpResponse(ret)

def boards_favorite(request):
    """이 API는 자유게시판, user의 Favorite 게시판, user의 cafe 게시판의 
    배열을 반환한다."""
    def join_list(list1, list2):
        return list1 + [item for item in list2 if item not in list1]
    
    oauth_token = request.REQUEST['oauth_token']
    user_id = Token.get_user_id(oauth_token)

    # add default
    default_list = ['board_freeboard']
    # add favorites
    favorites = Favorite.get_by_user(user_id)
    favorite_list = map(lambda x: x.get('board_id'), favorites)
    # add cafe
    cafe_boards = [Cafe.get_boards(cafe_id) for cafe_id 
                   in User.get_cafe(user_id)]
    cafe_board_list = reduce(lambda x, y: x + y, cafe_boards)
    
    # merge default, favorite, cafe list
    board_list = reduce(join_list, (default_list, favorite_list,
                                    cafe_board_list))
    # get boards
    boards = filter(None, map(Board.get_or_none, board_list))
    ret = dumps(boards)
    return HttpResponse(ret)
     
def boards_lookup(request):
    """This API returns array of boards
    
    * resource: 'boards/lookup'
    ** method: GET, oauth not required, rate limited
    ** mandatory parameter: board_id (comma separated)"""
    board_list = request.GET['board_id'].split(',')
    boards = map(Board.get, board_list)
    ret = dumps(boards)
    return HttpResponse(ret)

@csrf_exempt
@oauth_required
def comments_create(request, board_id=None, article_id=None):
    """This API posts a comment. 
    
    * resource: 'comments/create'
    ** method: POST, oauth required, rate limited
    ** mandatory parameter: board_id, article_id, message"""
    # read parameter
    try:
        if not board_id:
            board_id = request.POST['board_id']
        if not article_id:
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

@oauth_required
def users_lookup(request):
    """This API returns array of users
    
    * resource: 'users/lookup'
    ** method: GET, oauth required, rate limited
    ** mandatory parameter: user_id (comma separated)"""
    id_list = request.GET['user_id'].split(',')
    users = map(User.get, id_list)
    ret = dumps(users)
    return HttpResponse(ret)

@oauth_required
def users_show(request, user_id=None):
    """This API returns user
    
    * resource: 'users/show'
    ** method: GET, oauth required, rate limited
    ** mandatory parameter: user_id"""
    if not user_id:
        user_id = request.GET['user_id']
    user = User.get(user_id)
    ret = dumps(user)
    return HttpResponse(ret)

@oauth_required
def favorites_list(request):
    oauth_token = request.REQUEST['oauth_token']
    user_id = Token.get_user_id(oauth_token)
    favorites = Favorite.get_by_user(user_id)
    ret = dumps(favorites)
    return HttpResponse(ret)
    
    
def index(request):
    consumers = Consumer.objects.all()
    return render_to_response('index.html', {'consumers': consumers})
