import os
import datetime
import models
from apiprj.oauth_app.models import Token as OauthToken
from apiprj.settings import USER_IMG_PATH, USER_IMG_PREFIX

class ModelnameError(Exception):pass

class Board(object):
    @classmethod
    def pack(self, board, count=None, count24h=None):
        packed_board = {'board_id': board.tablename,
                        'title': board.title,
                        'description': board.description,
                        'admin': board.admin_id,
                        'count': count,
                        'count24h': count24h}
        return packed_board    
    
    @classmethod
    def get(self, board_id):
        # get boardinfo model object
        boardinfo = None
        if board_id.startswith('board'):
            boardinfo = models.Boardinfo.objects.get(tablename=board_id)
        elif board_id.startswith('photo'):
            boardinfo = models.Photoinfo.objects.get(tablename=board_id)
    
        # count articles
        board_model = Article.eval(board_id)
        time_window = datetime.datetime.today() - datetime.timedelta(days=1)
        count = board_model.objects.count()
        count24h = board_model.objects.filter(reg_date__gt=time_window).count()
        
        # return json object
        board = Board.pack(boardinfo, count=count, count24h=count24h)
        return board
    

class Comment(object):     
    @classmethod   
    def eval(self, board_id):
        comment_classname = "Comment" + board_id.title().replace('_', '')[5:]
        if comment_classname not in dir(models):
            raise ModelnameError
        return eval("models." + comment_classname)

    @classmethod
    def pack(self, cmt, board_id):
        packed_cmt = {'board_id': board_id,
                      'id': cmt.id,
                      'content': cmt.content,
                      'reg_date': cmt.reg_date.isoformat(),
                      'author': {'name': cmt.name,
                                 'id': cmt.user_id,
                                 'img_url': User.get_img_url(cmt.user_id)}}
        return packed_cmt
    
    @classmethod
    def get(self, board_id, article_id):
        comment_model = Comment.eval(board_id)
        comments = comment_model.objects.filter(idx=article_id)
        return map(lambda cmt: Comment.pack(cmt, board_id), comments)
    
    @classmethod
    def post(self, board_id, article_id, user_id, content):
        comment_model = Comment.eval(board_id)
        user_name = models.Member.objects.get(id=user_id).name
        cmt = comment_model(idx=article_id, user_id=user_id, name=user_name,
                            content=content, reg_date=datetime.datetime.today())
        cmt.save()

class Article(object):
    @classmethod
    def eval(self, board_id):
        board_classname = board_id.title().replace('_', '')
        if board_classname not in dir(models):
            raise ModelnameError
        return eval("models." + board_classname)

    @classmethod
    def pack(self, article, board_id, comments=[]):
        packed_article = {'board_id': board_id,
                          'id': article.id,
                          'author': {'name': article.name,
                                     'id': article.user_id,
                                     'img_url': User.get_img_url(article.user_id)},
                          'title': article.title,
                          'hits': article.count,
                          'reg_date': article.reg_date.isoformat(),
                          'content': article.content,
                          'file': article.file_name,
                          'comments': comments}
        return packed_article

    @classmethod
    def get(self, board_id, article_id):
        board_model = Article.eval(board_id)
        article_model = board_model.objects.get(id=article_id)
        comments = Comment.get(board_id, article_id)
        article = Article.pack(article_model, board_id, comments) 
        return article
    
    @classmethod
    def get_list(self, board_id, page=0, per_page=20):
        s = page * per_page
        e = s + per_page
        board_model = Article.eval(board_id)
        articles = board_model.objects.all().order_by('-reg_date')[s:e]
        return map(lambda article: Article.pack(article, board_id), articles)

class User(object):
    @classmethod
    def pack(self, user):
        packed_user = {'id': user.id,
                       'name': user.name,
                       'entrance_year': user.id_number,
                       'mobile': user.cell_phone,
                       'email': user.email,
                       'img_url': self.get_img_url(user.id)}
        return packed_user

    @classmethod
    def get_img_url(self, user_id):
        img_path = os.path.join(USER_IMG_PATH, user_id)
        if os.path.isfile(img_path):
            return USER_IMG_PREFIX + user_id
        else:
            return "http://s.twimg.com/a/1278188204/images/default_profile_0_normal.png"

    @classmethod
    def get(self, user_id):
        user = models.Member.objects.get(id=user_id)
        return self.pack(user)

class Token(object):
    @classmethod
    def get_user_id(self, oauth_token):
        return OauthToken.objects.get(key=oauth_token).user


    
