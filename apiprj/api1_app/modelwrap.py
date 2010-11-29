import os
import datetime
import models
from apiprj.oauth_app.models import Token
from apiprj.settings import USER_IMG_PATH, USER_IMG_PREFIX

class ModelnameError(Exception):pass

def eval_board(board_id):
    board_classname = board_id.title().replace('_', '')
    if board_classname not in dir(models):
        raise ModelnameError
    return eval("models." + board_classname)

def eval_comment(board_id):
    comment_classname = "Comment" + board_id.title().replace('_', '')[5:]
    if comment_classname not in dir(models):
        raise ModelnameError
    return eval("models." + comment_classname)

def pack_comment(cmt, board_id):
    packed_cmt = {'board_id': board_id,
                  'id': cmt.id,
                  'content': cmt.content,
                  'reg_date': cmt.reg_date.isoformat(),
                  'author': {'name': cmt.name,
                             'id': cmt.user_id,
                             'img_url': get_user_img_url(cmt.user_id)}}
    return packed_cmt

def pack_article(article, board_id, comments=[]):
    packed_article = {'board_id': board_id,
                      'id': article.id,
                      'author': {'name': article.name,
                                 'id': article.user_id,
                                 'img_url': get_user_img_url(article.user_id)},
                      'title': article.title,
                      'hits': article.count,
                      'reg_date': article.reg_date.isoformat(),
                      'content': article.content,
                      'file': article.file_name,
                      'comments': comments}
    return packed_article

def pack_board(board, count=None, count24h=None):
    packed_board = {'board_id': board.tablename,
                    'title': board.title,
                    'description': board.description,
                    'admin': board.admin_id,
                    'count': count,
                    'count24h': count24h}
    return packed_board

def pack_user(user):
    packed_user = {'id': user.id,
                   'name': user.name,
                   'entrance_year': user.id_number,
                   'mobile': user.cell_phone,
                   'email': user.email,
                   'img_url': get_user_img_url(user.id)}
    return packed_user

def get_user_img_url(user_id):
    img_path = os.path.join(USER_IMG_PATH, user_id)
    if os.path.isfile(img_path):
        return USER_IMG_PREFIX + user_id
    else:
        return "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png"

def get_user(user_id):
    user = models.Member.objects.get(id=user_id)
    return pack_user(user)

def get_comments(board_id, article_id):
    comment_model = eval_comment(board_id)
    comments = comment_model.objects.filter(idx=article_id)
    return map(lambda cmt: pack_comment(cmt, board_id), comments)

def post_comments(board_id, article_id, user_id, content):
    comment_model = eval_comment(board_id)
    user_name = models.Member.objects.get(id=user_id).name
    cmt = comment_model(idx=article_id, user_id=user_id, name=user_name,
                        content=content, reg_date=datetime.datetime.today())
    cmt.save()

def get_article(board_id, article_id):
    board_model = eval_board(board_id)
    article_model = board_model.objects.get(id=article_id)
    comments = get_comments(board_id, article_id)
    article = pack_article(article_model, board_id, comments) 
    return article

def get_articles(board_id, page=0, per_page=20):
    s = page * per_page
    e = s + per_page
    board_model = eval_board(board_id)
    articles = board_model.objects.all().order_by('-reg_date')[s:e]
    return map(lambda article: pack_article(article, board_id), articles)

def get_board(board_id):
    # get boardinfo model object
    boardinfo = None
    if board_id.startswith('board'):
        boardinfo = models.Boardinfo.objects.get(tablename=board_id)
    elif board_id.startswith('photo'):
        boardinfo = models.Photoinfo.objects.get(tablename=board_id)

    # count articles
    board_model = eval_board(board_id)
    time_window = datetime.datetime.today() - datetime.timedelta(days=1)
    count = board_model.objects.count()
    count24h = board_model.objects.filter(reg_date__gt=time_window).count()
    
    # return json object
    board = pack_board(boardinfo, count=count, count24h=count24h)
    return board

def get_user_id_from_token(oauth_token):
    return Token.objects.get(key=oauth_token).user
    
