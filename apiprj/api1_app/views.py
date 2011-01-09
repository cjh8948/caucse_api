#! -*- coding: utf8 -*- 
from apiprj.oauth_app.models import Consumer
from apiprj.oauth_app.models import Token as TokenModel
from apiprj.oauth_app.utils.decorators import oauth_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.simplejson import dumps
from django.views.decorators.csrf import csrf_exempt
from utils.decorators import api_exception
from modelwrap import Article, Board, Comment, User, Token, Favorite, Cafe
from apiprj.exceptions import NotImplementedYet

@csrf_exempt 
@api_exception
@oauth_required
def articles_create(request, oauth_params, board_id=None):
    """This API posts an article.
    
    * resource: 'articles/create'
    ** method: POST, oauth required, rate limited
    ** mandatory parameter: board_id, title, message"""
    if not board_id:
        board_id = request.POST['board_id']
    title = request.POST['title']
    message = request.POST['message']
    oauth_token = request.POST['oauth_token']    
    if board_id.startswith('photo'):
        raise NotImplementedYet('사진게시판 게시 기능은 지원하지 않습니다.')
    
    user_id = Token.get_user_id(oauth_token)
    article = Article.post(board_id=board_id, user_id=user_id, title=title,
                           message=message)

    # return result
    ret = dumps({'status':'ok', 'article': article})    
    return HttpResponse(ret)

@csrf_exempt 
@api_exception
@oauth_required
def articles_update(request, oauth_params, board_id=None, article_id=None):
    """This API posts an article.
    
    * resource: 'articles/create'
    ** method: POST, oauth required, rate limited
    ** mandatory parameter: board_id, title, message"""
    if not board_id:
        board_id = request.POST['board_id']
    if not article_id:
        article_id = request.POST['article_id']
    title = request.POST['title']
    message = request.POST['message']
    oauth_token = request.POST['oauth_token']    
    if board_id.startswith('photo'):
        raise NotImplementedYet('사진게시판 게시 기능은 지원하지 않습니다.')
    
    user_id = Token.get_user_id(oauth_token)
    article = Article.update(board_id=board_id, article_id=article_id,
                             user_id=user_id, title=title, message=message)

    # return result
    ret = dumps({'status':'ok', 'article': article})    
    return HttpResponse(ret)

@api_exception
@oauth_required
def articles_delete(request, oauth_params, board_id=None, article_id=None):
    if not board_id:
        board_id = request.GET['board_id']
    if not article_id:
        article_id = int(request.GET['article_id'])
    oauth_token = request.REQUEST['oauth_token']
    if board_id.startswith('photo'):
        raise NotImplementedYet('사진게시판 게시물 삭제 기능은 지원하지 않습니다.')
    
    user_id = Token.get_user_id(oauth_token)
    Article.delete(board_id, article_id, user_id)
    ret = dumps({'status':'ok'})
    return HttpResponse(ret)
    
@api_exception
@oauth_required
def articles_list(request, oauth_params, board_id=None):
    """This API returns array of articles and list option. 
    
    * resource: 'articles/list'
    ** method: GET, oauth required, rate limited
    ** mandatory parameter: board_id
    ** optional parameter: page(default=0), per_page(default=20)"""
    page = 0
    per_page = 20
    q = ""
    
    # get request parameter
    if not board_id:
        board_id = request.GET['board_id']

    if request.GET.has_key('page'):
        page = int(request.GET['page'])
    if request.GET.has_key('per_page'):
        per_page = int(request.GET['per_page'])
    if request.GET.has_key('q'):
        q = request.GET['q']

    # make json object to return
    listinfo, articles = Article.get_list(board_id, page, per_page, q)

    ret_item = {'listinfo': listinfo, 'articles': articles}
    ret = dumps(ret_item)

    return HttpResponse(ret)

@api_exception
@oauth_required
def articles_show(request, oauth_params, board_id=None, article_id=None):
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

@api_exception
@oauth_required
def boards_favorite(request, oauth_params):
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
    cafe_board_list = []
    cafe_boards = [Cafe.get_boards(cafe_id) for cafe_id 
                   in User.get_cafe(user_id)]
    if cafe_boards:
        cafe_board_list = reduce(lambda x, y: x + y, cafe_boards)
    
    # merge default, favorite, cafe list
    board_list = reduce(join_list, (default_list, favorite_list,
                                    cafe_board_list))
    # get boards
    boards = filter(None, map(Board.get_or_none, board_list))
    ret = dumps(boards)
    return HttpResponse(ret)

@api_exception     
def boards_lookup(request, **kw):
    """This API returns array of boards
    
    * resource: 'boards/lookup'
    ** method: GET, oauth not required, rate limited
    ** mandatory parameter: board_id (comma separated)"""
    board_list = request.GET['board_id'].split(',')
    boards = map(Board.get, board_list)
    ret = dumps(boards)
    return HttpResponse(ret)

@csrf_exempt
@api_exception
@oauth_required
def comments_create(request, oauth_params, board_id=None, article_id=None):
    """This API posts a comment. 
    
    * resource: 'comments/create'
    ** method: POST, oauth required, rate limited
    ** mandatory parameter: board_id, article_id, message"""
    # read parameter
    if not board_id:
        board_id = request.POST['board_id']
    if not article_id:
        article_id = request.POST['article_id']
    message = request.POST['message']
    oauth_token = request.POST['oauth_token']
    
    # update comment
    user_id = Token.get_user_id(oauth_token)
    cmt = Comment.post(board_id=board_id, article_id=article_id,
                       user_id=user_id, content=message)
    
    # return result
    ret = dumps({'status':'ok', 'comment':cmt})    
    return HttpResponse(ret)


@api_exception
@oauth_required
def comments_delete(request, oauth_params, board_id=None, comment_id=None):
    if not board_id:
        board_id = request.GET['board_id']
    if not comment_id:
        comment_id = int(request.GET['comment_id'])
    oauth_token = request.REQUEST['oauth_token']
    user_id = Token.get_user_id(oauth_token)
    Comment.delete(board_id, comment_id, user_id)
    ret = dumps({'status':'ok'})
    return HttpResponse(ret)

@api_exception
@oauth_required
def users_lookup(request, oauth_params):
    """This API returns array of users
    
    * resource: 'users/lookup'
    ** method: GET, oauth required, rate limited
    ** mandatory parameter: user_id (comma separated)"""
    id_list = request.GET['user_id'].split(',')
    users = map(User.get, id_list)
    ret = dumps(users)
    return HttpResponse(ret)

@api_exception
@oauth_required
def users_show(request, oauth_params, user_id=None):
    """This API returns user
    
    * resource: 'users/show'
    ** method: GET, oauth required, rate limited"""
    if not user_id:
        if request.GET.has_key('user_id'):
            user_id = request.GET['user_id']
        else:
            oauth_token = request.REQUEST['oauth_token']
            user_id = Token.get_user_id(oauth_token)
    user = User.get(user_id)
    ret = dumps(user)
    return HttpResponse(ret)

@api_exception
@oauth_required
def users_search(request, oauth_params):
    q = request.GET['q']
    users = User.search(q)
    ret = dumps(users)
    return HttpResponse(ret)

@api_exception
@oauth_required
def favorites_list(request, oauth_params):
    oauth_token = request.REQUEST['oauth_token']
    user_id = Token.get_user_id(oauth_token)
    favorites = Favorite.get_by_user(user_id)
    ret = dumps(favorites)
    return HttpResponse(ret)

def index(request):
    return render_to_response('index.html', {'user': request.user})

def apistatus(request):
    return render_to_response('apistatus.html', {'user': request.user})

def apireference(request):
    return render_to_response('apireference.html', {'user': request.user})

@login_required
def myapp(request):
    consumers = Consumer.objects.filter(user_id=request.user.username)
    consumer_token = []
    for consumer in consumers:
        try:
            token = TokenModel.objects.filter(type='A')\
                                      .filter(consumer=consumer)\
                                      .filter(user=consumer.user_id)[0]
        except IndexError:
            token = None
        consumer_token.append((consumer, token))
    return render_to_response('myapp.html', {'user': request.user,
                                             'consumer_token': consumer_token})