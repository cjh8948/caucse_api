#! -*- coding: utf8 -*- 
from apiprj.oauth_app.utils.decorators import oauth_required
from apiprj.exceptions import (NotImplementedYet, ParameterIsNotValid, 
                               RequiredParameterDoesNotExist, NoMatchingResult,
                               AuthError)
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.utils.simplejson import dumps
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admindocs import utils
from django.contrib.admindocs.views import (get_root_path, 
                                            missing_docutils_page,
                                            extract_views_from_urlpatterns,
                                            simplify_regex)

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.importlib import import_module
from django.utils.translation import ugettext as _
from modelwrap import Article, Board, Comment, User, Token, Favorite, Cafe
from utils.decorators import api_exception
from django.core import urlresolvers
import urls

@csrf_exempt 
@api_exception
@oauth_required
def articles_create(request, oauth_params, board_id=None):
    r"""
    게시물을 등록하고 결과를 json 포맷으로 반환

    resource
     * /articles/create/<board_id> 
     
    method
     * POST
     * oauth required

    parameters (bold체는 필수)
     * **title**
     * **message**     
    
    note
     * 사진게시판은 지원하지 않는다.    

    example
     아래와 같이 요청하면,
    
     .. parsed-literal::
    
       POST /articles/create/board_test HTTP/1.1 
       Host: api.caucse.net
       Content-Type: application/x-www-form-urlencoded
       title=...&message=...

     성공시에는 다음과 같은 결과를 얻는다.
    
     .. parsed-literal::

       HTTP/1.0 200 OK
       Content-Type: text/html; charset=utf-8

       {
           "status": "ok", 
           "article": {
               "board_id": "board_alumni99", 
               "hits": 0, 
               "total_comments": 0, 
               "author": {
                   "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                   "name": "\\uc774\\ub355\\uc900", 
                   "id": "gochi"
               }, 
               "title": "title", 
               "comments": [], 
               "content": "message \\ud55c\\uae00 \\uba54\\uc2dc\\uc9c0 \\ud14c\\uc2a4\\ud2b8.", 
               "reg_date": "2011-01-19T13:24:08.949779", 
               "file": "", 
               "id": 3514
           }
       }
        
    실패시에는 다음과 같은 결과를 얻는다.
    
    .. parsed-literal::

       HTTP/1.0 200 OK
       Content-Type: text/html; charset=utf-8   
       
       {
           "status": "error", 
           "message": "\\uc0ac\\uc9c4\\uac8c\\uc2dc\\ud310 \\uac8c\\uc2dc \\uae30\\ub2a5\\uc740 \\uc9c0\\uc6d0\\ud558\\uc9c0 \\uc54a\\uc2b5\\ub2c8\\ub2e4.", 
           "type": "<type 'exceptions.NotImplementedError'>"
       }     
    """
    try:
        if not board_id:
            board_id = request.POST['board_id']
        title = request.POST['title']
        message = request.POST['message']
    except KeyError as e:
        raise RequiredParameterDoesNotExist(e)
    
    oauth_token = request.POST['oauth_token']    
    if board_id.startswith('photo'):
        raise NotImplementedYet('사진게시판 게시 기능은 지원하지 않습니다.')
    
    user_id = Token.get_user_id(oauth_token)
    article = Article.post(board_id=board_id, user_id=user_id, title=title,
                           message=message)

    # return result
    ret = dumps({'status':'ok', 'article': article})    
    return HttpResponse(ret)


@api_exception
@oauth_required
def articles_delete(request, oauth_params, board_id=None, article_id=None):
    r"""
    게시물을 삭제한다.

    resource
     * /articles/delete/<board_id>/<article_id> 
    
    method
     * GET
     * oauth required
    
    note
     * 사진게시판은 지원하지 않음
     * 인증된 사용자 본인의 게시물만 삭제 가능 
     
    example
     아래 요청을 보내면, (oauth 서명 포함)

     .. parsed-literal::
         
       GET /articles/delete/board_test/20 HTTP/1.1
      
     해당 게시물을 삭제하고 다음과 같은 결과를 반환한다.
    
     .. parsed-literal::
       
       HTTP/1.0 200 OK
       Content-Type: text/html; charset=utf-8   
       
       {
           "status": "ok"
       }       
    """ 
    try:   
        if not board_id:
            board_id = request.GET['board_id']
        if not article_id:
            article_id = int(request.GET['article_id'])
    except KeyError as e:
        raise RequiredParameterDoesNotExist(e)
    
    try:    
        oauth_token = request.REQUEST['oauth_token']
    except KeyError as e:
        raise AuthError(e)

    if board_id.startswith('photo'):
        raise NotImplementedYet('사진게시판 게시물 삭제 기능은 지원하지 않습니다.')
    
    user_id = Token.get_user_id(oauth_token)
    Article.delete(board_id, article_id, user_id)
    ret = dumps({'status':'ok'})
    return HttpResponse(ret)

@api_exception
@oauth_required
def articles_list(request, oauth_params, board_id=None):
    """
    질의 조건에 맞는 게시물의 리스트의 배열과 관련 정보를 반환한다.

    resource
     * /articles/list/<board_id>

    method
     * GET
     * oauth required
    
    parameters
     * page (default=0)
     * per_page (default=20)
     * q (default=""): 검색 질의어
    """
    page = 0
    per_page = 20
    q = ""
    
    # get request parameter
    try:
        if not board_id:
            board_id = request.GET['board_id']
    except KeyError as e:
        raise RequiredParameterDoesNotExist(e)

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
    """
    게시물의 내용을 보여준다.
    
    resorce
     * /articles/show/<board_id>/<article_id>
     
    method
     * GET
     * oauth required
    """
    if not board_id:
        board_id = request.GET['board_id']
    if not article_id:
        article_id = int(request.GET['article_id'])
    article = Article.get(board_id, article_id)
    ret = dumps(article) 
    return HttpResponse(ret)

@csrf_exempt 
@api_exception
@oauth_required
def articles_update(request, oauth_params, board_id=None, article_id=None):
    """
    게시물을 수정한다.

    method
     * POST
     * oauth required
    
    parameters (bold체는 필수)
     * **board_id**
     * **title**
     * **message**
    """
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
def boards_favorite(request, oauth_params):
    """즐겨찾기 게시판(자유게시판과 가입한 cafe의 게시판을 포함)들의 정보를 
    배열로 반환한다.
    
    method
     * GET
     * oauth required    
    """
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
    """게시판 정보를 배열로 반환한다.
    
    method
     * GET 
     * oauth not required

    parameter (bold체는 필수)
     * **board_id**: comma separated string (ex: "board_alumni99,photo_alumni99")
    """
    board_list = request.GET['board_id'].split(',')
    boards = map(Board.get, board_list)
    ret = dumps(boards)
    return HttpResponse(ret)

@csrf_exempt
@api_exception
@oauth_required
def comments_create(request, oauth_params, board_id=None, article_id=None):
    """게시물에 댓글을 단다.
    
    method
     * POST 
     * oauth required

    parameter (bold체는 필수)
     * **board_id**
     * **article_id**
     * **message**
    """
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
    """댓글을 삭제한다.
    
    method
     * GET 
     * oauth required

    parameter (bold체는 필수)
     * **board_id**
     * **comment_id**
    """
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
    """사용자 정보를 배열로 반환한다.
    
    method
     * GET
     * oauth required
    
    parameter (bold체는 필수)
     * **user_id**: comma separated string (ex: "gochi,jeppy,reset"), 최대 100명
    """
    id_list = request.GET['user_id'].split(',')
    if len(id_list) > 100:
        raise ParameterIsNotValid("한 번에 100명 이상을 조회할 수 없습니다.")
    
    try:
        users = map(User.get, id_list)
    except ObjectDoesNotExist:
        raise ParameterIsNotValid("user_id 파라미터에 유효하지 않은 값이 포함되어있습니다.")
    
    ret = dumps(users)
    return HttpResponse(ret)

@api_exception
@oauth_required
def users_show(request, oauth_params, user_id=None):
    """사용자 정보를 반환한다.
    
    method
     * GET
     * oauth required
    
    parameter (bold체는 필수)
     * user_id: user_id가 생략되면 oauth 인증된 사용자의 id로 대체된다.
    """
    if not user_id:
        if request.GET.has_key('user_id'):
            user_id = request.GET['user_id']
        else:
            oauth_token = request.REQUEST['oauth_token']
            user_id = Token.get_user_id(oauth_token)
    
    try:
        user = User.get(user_id)
    except ObjectDoesNotExist:
        raise ParameterIsNotValid("user_id가 올바르지 않습니다.")
    
    ret = dumps(user)
    return HttpResponse(ret)

@api_exception
@oauth_required
def users_search(request, oauth_params):
    """사용자 검색 결과를 반환한다.
    
    method
     * GET
     * oauth required
    
    parameter (bold체는 필수)
     * **q**: 검색어를 화이트 스페이스를 기준으로 나누어, 숫자인 경우 학번으로, 영문인 경우 아이디 및 이름으로, 한글인 경우 이름으로 검색함.
    
    note
     * 결과는 최대 200건을 반환한다.
    """    
    try:
        q = request.GET['q']
    except KeyError as e:
        raise RequiredParameterDoesNotExist(e)
    
    try:
        users = User.search(q)
    except NoMatchingResult:
        users = []
        
    ret = dumps(users[:200])
    return HttpResponse(ret)

@api_exception
@oauth_required
def favorites_list(request, oauth_params):
    oauth_token = request.REQUEST['oauth_token']
    user_id = Token.get_user_id(oauth_token)
    favorites = Favorite.get_by_user(user_id)
    ret = dumps(favorites)
    return HttpResponse(ret)

def view_index(request):
    if not utils.docutils_is_available:
        return missing_docutils_page(request)

    views = []
    view_functions = extract_views_from_urlpatterns(urls.urlpatterns)
    for (func, regex) in view_functions:
        views.append({
            'name': getattr(func, '__name__', func.__class__.__name__),
            'module': func.__module__,
            'url': simplify_regex(regex),
        })
    
    return render_to_response('doc/view_index.tpl', {
        'root_path': get_root_path(),
        'views': views
    }, context_instance=RequestContext(request))
    
def view_detail(request, view):
    if not utils.docutils_is_available:
        return missing_docutils_page(request)

    mod, func = urlresolvers.get_mod_func(view)
    try:
        view_func = getattr(import_module(mod), func)
    except (ImportError, AttributeError):
        raise Http404
    title, body, metadata = utils.parse_docstring(view_func.__doc__)
    if title:
        title = utils.parse_rst(title, 'view', _('view:') + view)
    if body:
        body = utils.parse_rst(body, 'view', _('view:') + view)
    for key in metadata:
        metadata[key] = utils.parse_rst(metadata[key], 'model', _('view:') + view)
    
    name = view.split('.')[-1].replace('_','/')
    return render_to_response('doc/view_detail.tpl', {
        'root_path': get_root_path(),
        'name': name,
        'summary': title,
        'body': body,
        'meta': metadata,
    }, context_instance=RequestContext(request))