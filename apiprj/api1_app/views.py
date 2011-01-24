#! -*- coding: utf8 -*- 
from apiprj.oauth_app.utils.decorators import oauth_required
from apiprj.exceptions import (NotImplementedYet, ParameterIsNotValid, 
                               RequiredParameterDoesNotExist, NoMatchingResult,
                               AuthError)
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.utils.simplejson import dumps
from django.views.decorators.csrf import csrf_exempt
from modelwrap import Article, Board, Comment, User, Token, Favorite, Cafe
from utils.decorators import api_exception

@csrf_exempt 
@api_exception
@oauth_required
def articles_create(request, oauth_params, board_id=None):
    r"""
    **/articles/create/<board_id>**
    
    게시물을 등록

    method
     * POST
     * oauth required

    parameters
     * **title** (필수)
     * **message** (필수)     
    
    note
     * 사진게시판은 지원하지 않는다.    

    example
     * request (oauth 인증 관련 parameter는 예제에서 생략)
         .. parsed-literal::
        
           POST /articles/create/board_test HTTP/1.1 
           Host: api.caucse.net
           Content-Type: application/x-www-form-urlencoded
           title=...&message=...

     * response (success case) 
         .. parsed-literal::

           HTTP/1.0 200 OK
           Content-Type: application/json; charset=utf-8
    
           {
              "status": "ok", 
              "article": {
                  "board_id": "board_alumni99", 
                  "hits": 0, 
                  "total_comments": 0, 
                  "author": {
                      "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                      "name": "이덕준", 
                      "id": "gochi"
                  }, 
                  "title": "title", 
                  "comments": [], 
                  "content": "message 한글 메시지 테스트.", 
                  "reg_date": "2011-01-20T09:16:13.394124", 
                  "file": "", 
                  "id": 3591
              }
           }
        
     * response (failure case) 
         .. parsed-literal::
    
           HTTP/1.0 200 OK
           Content-Type: application/json; charset=utf-8
              
           {
                "status": "error", 
                "message": "사진게시판 게시 기능은 지원하지 않습니다.", 
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
    
    oauth_token = oauth_params['oauth_token']    
    if board_id.startswith('photo'):
        raise NotImplementedYet('사진게시판 게시 기능은 지원하지 않습니다.')
    
    user_id = Token.get_user_id(oauth_token)
    article = Article.post(board_id=board_id, user_id=user_id, title=title,
                           message=message)

    # return result
    ret = dumps({'status':'ok', 'article': article})    
    return HttpResponse(ret, content_type='application/json')


@api_exception
@oauth_required
def articles_delete(request, oauth_params, board_id=None, article_id=None):
    r"""
    **/articles/delete/<board_id>/<article_id>** 
   
    게시물을 삭제

    method
     * DELETE
     * oauth required
    
    note
     * 사진게시판은 지원하지 않음
     * 인증된 사용자 본인의 게시물만 삭제 가능 
     
    example
     * request (oauth 인증 관련 parameter는 예제에서 생략)
        .. parsed-literal::

            DELETE /articles/delete/board_test/20 HTTP/1.1
      
     * response (success case) 
        .. parsed-literal::
          
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8   
            
            {
                "status": "ok"
            }       
    """ 
    try:    
        oauth_token = oauth_params['oauth_token']
    except KeyError as e:
        raise AuthError(e)

    if board_id.startswith('photo'):
        raise NotImplementedYet('사진게시판 게시물 삭제 기능은 지원하지 않습니다.')
    
    user_id = Token.get_user_id(oauth_token)
    Article.delete(board_id, article_id, user_id)
    ret = dumps({'status':'ok'})
    return HttpResponse(ret, content_type='application/json')

@api_exception
@oauth_required
def articles_list(request, oauth_params, board_id=None):
    """
    **/articles/list/<board_id>**
    
    게시물의 리스트와 질의 조건를 반환

    method
     * GET
     * oauth required
    
    parameters
     * page (default=0): 0 부터 count
     * per_page (default=20): 한 페이지에 조회할 게시물 갯수
     * q (default=""): 제목, 내용, 이름, id 를 검색할 검색어

    example
     * request (oauth parameter는 예제에서 생략)
             .. parsed-literal::
           
                GET /articles/list/board_test?page=2&per_page=15&q=... HTTP/1.1  
                    
     * response
            .. parsed-literal::
           
                HTTP/1.0 200 OK
                Content-Type: application/json; charset=utf-8   
                   
                {
                    "articles": [
                        {
                            "board_id": "board_alumni99", 
                            "hits": 0, 
                            "total_comments": 0, 
                            "author": {
                                "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                                "name": "이덕준", 
                                "id": "gochi"
                            }, 
                            "title": "title", 
                            "comments": [], 
                            "content": "message 한글 메시지 테스트.", 
                            "reg_date": "2011-01-20T09:21:17", 
                            "file": "", 
                            "id": 3595
                        }, 
                
                        ...
                
                        {
                            "board_id": "board_alumni99", 
                            "hits": 0, 
                            "total_comments": 0, 
                            "author": {
                                "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                                "name": "이덕준", 
                                "id": "gochi"
                            }, 
                            "title": "title!!!", 
                            "comments": [], 
                            "content": "message changed!!!!!", 
                            "reg_date": "2011-01-20T09:12:08", 
                            "file": "", 
                            "id": 3574
                        }
                    ], 
                    "listinfo": {
                        "board_id": "board_alumni99", 
                        "board_title": "99학번 게시판", 
                        "total_articles": 3382, 
                        "total_pages": 169, 
                        "total_matched_articles": 3382, 
                        "q": "", 
                        "per_page": 20, 
                        "page": 0
                    }
                }    
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

    return HttpResponse(ret, content_type='application/json')

@api_exception
@oauth_required
def articles_show(request, oauth_params, board_id=None, article_id=None):
    r"""
    **/articles/show/<board_id>/<article_id>**
    
    게시물 및 게시물에 달린 커멘트의 내용을 반환

    method
     * GET
     * oauth required
     
    example
     * response (oauth 인증 관련 parameter는 예제에서 생략)
         .. parsed-literal::
           
           GET /articles/show/board_test/100 HTTP/1.1
               
     * response
         .. parsed-literal::
           
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8   
                   
            {
                "board_id": "board_alumni99", 
                "hits": 28, 
                "total_comments": 3, 
                "author": {
                    "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                    "name": "이덕준", 
                    "id": "gochi"
                }, 
                "title": "RE : 수학여행!!!", 
                "comments": [
                    {
                        "board_id": "board_alumni99", 
                        "content": "커멘트 테스트 하는 중....", 
                        "reg_date": "2011-01-19", 
                        "id": 17253, 
                        "author": {
                            "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                            "name": "이덕준", 
                            "id": "gochi"
                        }
                    }, 
                    {
                        "board_id": "board_alumni99", 
                        "content": "커멘트 테스트 하는 중....", 
                        "reg_date": "2011-01-19", 
                        "id": 17254, 
                        "author": {
                            "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                            "name": "이덕준", 
                            "id": "gochi"
                        }
                    }, 
                    {
                        "board_id": "board_alumni99", 
                        "content": "커멘트 테스트 하는 중....", 
                        "reg_date": "2011-01-19", 
                        "id": 17255, 
                        "author": {
                            "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                            "name": "이덕준", 
                            "id": "gochi"
                        }
                    }
                ], 
                "content": "수학여행 가자고~~", 
                "reg_date": "2001-04-05T22:55:23", 
                "file": "", 
                "id": 100
            }     
    """
    if not board_id:
        board_id = request.GET['board_id']
    if not article_id:
        article_id = int(request.GET['article_id'])
    article = Article.get(board_id, article_id)
    ret = dumps(article) 
    return HttpResponse(ret, content_type='application/json')

@csrf_exempt 
@api_exception
@oauth_required
def articles_update(request, oauth_params, board_id=None, article_id=None):
    """
    **/articles/update/<board_id>/<article_id>**
    
    게시물을 수정

    method
     * POST
     * oauth required
    
    parameters
     * **title** (필수)
     * **message** (필수)

    example
     * request (oauth 인증 관련 parameter는 예제에서 생략)
        .. parsed-literal::
        
            POST /articles/update/board_alumni99/3598 HTTP/1.1
            Host: api.caucse.net
            Content-Type: application/x-www-form-urlencoded
            title=...&message=...     

     * response
        .. parsed-literal::
        
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8   
                 
            {
                "status": "ok", 
                "article": {
                    "board_id": "board_alumni99", 
                    "hits": 0, 
                    "total_comments": 0, 
                    "author": {
                        "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                        "name": "이덕준", 
                        "id": "gochi"
                    }, 
                    "title": "title!!!", 
                    "comments": [], 
                    "content": "message changed!!!!!", 
                    "reg_date": "2011-01-20T09:21:18", 
                    "file": "", 
                    "id": 3598
                }
            }     
    """
    if not board_id:
        board_id = request.POST['board_id']
    if not article_id:
        article_id = request.POST['article_id']
    title = request.POST['title']
    message = request.POST['message']
    oauth_token = oauth_params['oauth_token']    
    if board_id.startswith('photo'):
        raise NotImplementedYet('사진게시판 게시 기능은 지원하지 않습니다.')
    
    user_id = Token.get_user_id(oauth_token)
    article = Article.update(board_id=board_id, article_id=article_id,
                             user_id=user_id, title=title, message=message)

    # return result
    ret = dumps({'status':'ok', 'article': article})    
    return HttpResponse(ret, content_type='application/json')
    
@api_exception
@oauth_required
def boards_favorite(request, oauth_params):
    r"""
    **/boards/favorite**
    
    즐겨찾는 게시판 리스트 반환 
    
    method
     * GET
     * oauth required    
    
    note
     * 즐겨찾는 게시판은 즐겨찾기 등록된 게시판 및 자유게시판과 가입한 cafe의 게시판을 포함한다.
     
    example
     * request (oauth parameter는 예제에서 생략)
        .. parsed-literal::

            GET /boards/favorite HTTP/1.1     

     * response
        .. parsed-literal::
       
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  
            
            [
                {
                    "board_id": "board_freeboard", 
                    "count": 10147, 
                    "description": "", 
                    "title": "자유게시판", 
                    "admin": "anjae83", 
                    "count24h": 0
                }, 
                
                ...
                
                {
                    "board_id": "photo_part_plan", 
                    "count": 1670, 
                    "description": "", 
                    "title": "기획총무부 사진 게시판", 
                    "admin": "hyojeong28", 
                    "count24h": 0
                }
            ]                 
    """
    def join_list(list1, list2):
        return list1 + [item for item in list2 if item not in list1]
    
    oauth_token = oauth_params['oauth_token']
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
    return HttpResponse(ret, content_type='application/json')

@api_exception     
def boards_lookup(request, **kw):
    """
    **/boards/lookup**
    
    게시판 리스트 반환

    method
     * GET  

    parameter
     * **board_id** (필수): comma(%2C) separated string
     
    example
     * request
        .. parsed-literal::

            GET /boards/lookup?board_id=board_alumni99%2Cboard_alumni00 HTTP/1.1
            
     * response
        .. parsed-literal::
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  

            [
                {
                    "board_id": "board_alumni99", 
                    "count": 3225, 
                    "description": "", 
                    "title": "99학번 게시판", 
                    "admin": "hipbrain", 
                    "count24h": 0
                }, 
                {
                    "board_id": "board_alumni00", 
                    "count": 4041, 
                    "description": "", 
                    "title": "00학번 게시판", 
                    "admin": "alsrnwkd", 
                    "count24h": 0
                }
            ]
    """
    board_list = request.GET['board_id'].split(',')
    boards = map(Board.get, board_list)
    ret = dumps(boards)
    return HttpResponse(ret, content_type='application/json')

@csrf_exempt
@api_exception
@oauth_required
def comments_create(request, oauth_params, board_id=None, article_id=None):
    r"""
    **/comments/create/<board_id>/<article_id>**
    
    커멘트 생성
    
    method
     * POST 
     * oauth required

    parameters
     * **message** (필수)
     
    example
     * request
        .. parsed-literal::

            POST /comments/create/board_alumni99/100 HTTP/1.1
            Host: api.caucse.net
            Content-Type: application/x-www-form-urlencoded
            message=...            
            
     * response (성공)
        .. parsed-literal::
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  
     
            {
                "status": "ok", 
                "comment": {
                    "board_id": "board_alumni99", 
                    "content": "restful comment test", 
                    "reg_date": "2011-01-20T09:21:18.378891", 
                    "id": 17311, 
                    "author": {
                        "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                        "name": "이덕준", 
                        "id": "gochi"
                    }
                }
            }

     * response (실패)        
        .. parsed-literal::        
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  
            
            {
                "status": "error", 
                "message": "BoardNotRegistered", 
                "type": "<class 'apiprj.exceptions.DatabaseTableDoesNotExist'>"
            }        
    """
    # read parameter
    if not board_id:
        board_id = request.POST['board_id']
    if not article_id:
        article_id = request.POST['article_id']
    message = request.POST['message']
    oauth_token = oauth_params['oauth_token']
    
    # update comment
    user_id = Token.get_user_id(oauth_token)
    cmt = Comment.post(board_id=board_id, article_id=article_id,
                       user_id=user_id, content=message)
    
    # return result
    ret = dumps({'status':'ok', 'comment':cmt})    
    return HttpResponse(ret, content_type='application/json')

@api_exception
@oauth_required
def comments_delete(request, oauth_params, board_id=None, comment_id=None):
    """
    **/comments/delete/<board_id>/<comment_id>**
    
    커맨트 삭제
    
    method
     * DELETE 
     * oauth required
     
    example
     * request
        .. parsed-literal::

            DELETE /comments/delete/board_alumni99/1234 HTTP/1.1
            
     * response (성공)
        .. parsed-literal::
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  
     
            {
                "status": "ok"
            }

     * response (실패)        
        .. parsed-literal::        
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  
            
            {
                "status": "error", 
                "message": "BoardNotRegistered", 
                "type": "<class 'apiprj.exceptions.DatabaseTableDoesNotExist'>"
            }            
    """
    oauth_token = oauth_params['oauth_token']
    user_id = Token.get_user_id(oauth_token)
    Comment.delete(board_id, comment_id, user_id)
    ret = dumps({'status':'ok'})
    return HttpResponse(ret, content_type='application/json')

@api_exception
@oauth_required
def users_lookup(request, oauth_params):
    """
    **/users/lookup**
    
    여러 사용자 조회 
    
    method
     * GET 
     * oauth required

    parameter
     * **user_id** (필수): comma(%2C) separated string (ex: "gochi,reset")
     
    note
     * 조회 가능한 사용자는 최대 100명
     
    example
     * request
        .. parsed-literal::

            GET /users/lookup?user_id=gochi%2Creset HTTP/1.1
            
     * response (성공)
        .. parsed-literal::
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  
     
            [
                {
                    "name": "이덕준", 
                    "mobile": "123-4567-8900", 
                    "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                    "introduce": "", 
                    "id": "gochi", 
                    "birthday": null, 
                    "messenger": "google talk : gochist@gmail.com", 
                    "homepage": "gochi.kr", 
                    "email": "gochi@caucse.net", 
                    "entrance_year": 1999
                }, 
                {
                    "name": "강석천", 
                    "mobile": null, 
                    "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                    "introduce": null, 
                    "id": "reset", 
                    "birthday": null, 
                    "messenger": null, 
                    "homepage": null, 
                    "email": null, 
                    "entrance_year": 1999
                }
            ]

     * response (실패)        
        .. parsed-literal::        
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  
            
            {
                "status": "error", 
                "message": "user_id 파라미터에 유효하지 않은 값이 포함되어있습니다.", 
                "type": "<class 'apiprj.exceptions.ParameterIsNotValid'>"
            }     
    """
    id_list = request.GET['user_id'].split(',')
    if len(id_list) > 100:
        raise ParameterIsNotValid("한 번에 100명 이상을 조회할 수 없습니다.")
    
    try:
        users = map(User.get, id_list)
    except ObjectDoesNotExist:
        raise ParameterIsNotValid("user_id 파라미터에 유효하지 않은 값이 포함되어있습니다.")
    
    ret = dumps(users)
    return HttpResponse(ret, content_type='application/json')

@api_exception
@oauth_required
def users_show(request, oauth_params, user_id=None):
    """
    **/users/show/<user_id>**
    
    사용자 조회 
    
    method
     * GET 
     * oauth required
     
    note
     * user_id 생략시, oauth 인증된 사용자 정보 반환
     
    example
     * request
        .. parsed-literal::

            GET /users/show/gochi HTTP/1.1
            
     * response (성공)
        .. parsed-literal::
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  

            {
                "name": "이덕준", 
                "mobile": "123-4567-8900", 
                "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                "introduce": "", 
                "id": "gochi", 
                "birthday": null, 
                "messenger": "google talk : gochist@gmail.com", 
                "homepage": "gochi.kr", 
                "email": "gochi@caucse.net", 
                "entrance_year": 1999
            }

     * response (실패)        
        .. parsed-literal::        
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  
            
            {
                "status": "error", 
                "message": "user_id가 올바르지 않습니다.", 
                "type": "<class 'apiprj.exceptions.ParameterIsNotValid'>"
            }     
            
    """
    if not user_id:
        if request.GET.has_key('user_id'):
            user_id = request.GET['user_id']
        else:
            oauth_token = oauth_params['oauth_token']
            user_id = Token.get_user_id(oauth_token)
    
    try:
        user = User.get(user_id)
    except ObjectDoesNotExist:
        raise ParameterIsNotValid("user_id가 올바르지 않습니다.")
    
    ret = dumps(user)
    return HttpResponse(ret, content_type='application/json')

@api_exception
@oauth_required
def users_search(request, oauth_params):
    """
    **/users/search**
    
    사용자 검색 
    
    method
     * GET 
     * oauth required
    
    parameter
     * **q** (필수): 검색 질의어
     
    note
     * 검색어를 화이트 스페이스를 기준으로 토큰화 하여, 토큰이 숫자인 경우 
       학번으로, 영문인 경우 아이디 및 이름으로, 한글인 경우 이름으로 분류,
       각 분류 내 OR 연산, 분류 별 AND 연산으로 검색함. (ex. q="99 98 준" : 
       1998 또는 1999 학번 중 이름에 '준'이라는 글자가 포함된 회원 검색) 
     * 학번을 두 자리로 입력한 경우, 50보다 작으면 20XX 학번으로, 50보다 
       크거나 같으면 19XX 학번으로 검색. 
     * 결과는 최대 200건을 반환한다.
     
    example
     * request
        .. parsed-literal::

            GET /users/show?q=99 HTTP/1.1
            
     * response (성공)
        .. parsed-literal::
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  

            [
                {
                    "name": "박종필", 
                    "mobile": "123-4567-8900", 
                    "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                    "introduce": "", 
                    "id": "jeppy", 
                    "birthday": null, 
                    "messenger": "MSN:jeppy99@nownuri.net", 
                    "homepage": "jeppy.cafe24.com", 
                    "email": "jeppy@caucse.net", 
                    "entrance_year": 1999
                }, 
                
                ...
                
                {
                    "name": "강석천", 
                    "mobile": null, 
                    "img_url": "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png", 
                    "introduce": null, 
                    "id": "reset", 
                    "birthday": null, 
                    "messenger": null, 
                    "homepage": null, 
                    "email": null, 
                    "entrance_year": 1999
                }
            ]
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
    return HttpResponse(ret, content_type='application/json')

@api_exception
@oauth_required
def favorites_list(request, oauth_params):
    """
    **/favorites/list**
    
    즐겨찾는 게시판(board_id) 및 우선순위 조회
    
    method
     * GET 
     * oauth required

    example
     * request
        .. parsed-literal::

            GET /favorites/list HTTP/1.1
            
     * response (성공)
        .. parsed-literal::
            
            HTTP/1.0 200 OK
            Content-Type: application/json; charset=utf-8  
     
            [
                {
                    "priority": 1, 
                    "board_id": "board_part_plan", 
                    "no": 413
                }, 
                {
                    "priority": 2, 
                    "board_id": "board_alumni99", 
                    "no": 416
                }, 
                {
                    "priority": 3, 
                    "board_id": "board_dongneteam", 
                    "no": 1243
                }, 
                {
                    "priority": 4, 
                    "board_id": "board_csesa", 
                    "no": 4684
                }
            ]
    """
    oauth_token = oauth_params['oauth_token']
    user_id = Token.get_user_id(oauth_token)
    favorites = Favorite.get_by_user(user_id)
    ret = dumps(favorites)
    return HttpResponse(ret, content_type='application/json')