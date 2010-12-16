import os, datetime, re
from apiprj.legacy_app import models
from apiprj.oauth_app.models import Token as OauthToken
from apiprj.settings import USER_IMG_PATH, USER_IMG_PREFIX
from django.db.models.aggregates import Max
from django.db.models import Q

class ModelnameError(Exception):pass

class Board(object):
    @classmethod
    def pack(self, boardinfo_model, count=None, count24h=None):
        packed_board = {'board_id': boardinfo_model.tablename,
                        'title': boardinfo_model.title,
                        'description': boardinfo_model.description,
                        'admin': boardinfo_model.admin_id,
                        'count': count,
                        'count24h': count24h}
        return packed_board
    
    @classmethod
    def get_or_none(self, board_id):
        try:
            return self.get(board_id)
        except Exception:
            return None    
    
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
        if board_id.startswith('board'):
            prefix = "Comment"
        else:
            prefix = "Memo"
        comment_classname = prefix + board_id.title().replace('_', '')[5:]
        if comment_classname not in dir(models):
            raise ModelnameError(comment_classname + ' ' + board_id)
        return eval("models." + comment_classname)

    @classmethod
    def pack(self, cmt_model, board_id):
        author = {'name': cmt_model.name,
                  'id': cmt_model.user_id,
                  'img_url': User.get_img_url(cmt_model.user_id)}

        packed_cmt = {'board_id': board_id,
                      'id': cmt_model.id,
                      'content': cmt_model.content,
                      'reg_date': cmt_model.reg_date.isoformat(),
                      'author': author}

        return packed_cmt
    
    @classmethod
    def get(self, board_id, article_id):
        comment_model = Comment.eval(board_id)
        comments = comment_model.objects.filter(idx=article_id)
        return map(lambda cmt: Comment.pack(cmt, board_id), comments)
    
    @classmethod
    def post(self, board_id, article_id, user_id, content):
        # check if article exists
        article_model = Article.eval(board_id)
        article_model.objects.get(id=article_id)

        # add comment            
        comment_model = Comment.eval(board_id)
        user_name = models.Member.objects.get(id=user_id).name
        cmt = comment_model(idx=article_id, user_id=user_id, name=user_name,
                            content=content,
                            reg_date=datetime.datetime.today())
        cmt.save()

class Article(object):
    @classmethod
    def eval(self, board_id):
        board_classname = board_id.title().replace('_', '')
        if board_classname not in dir(models):
            raise ModelnameError(board_classname + ' ' + board_id)
        return eval("models." + board_classname)

    @classmethod
    def pack(self, article_model, board_id, comments=[]):
        author = {'name': article_model.name, 'id': article_model.user_id,
                  'img_url': User.get_img_url(article_model.user_id)}
        packed_article = {'board_id': board_id,
                          'id': article_model.id,
                          'author': author,
                          'title': article_model.title,
                          'hits': article_model.count,
                          'reg_date': article_model.reg_date.isoformat(),
                          'content': article_model.content,
                          'file': article_model.file_name,
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
    def _get_query_from_natual_language(self, q):
        ids, titles, contents, names = [], [], [], []
        for token in q.split():
            ids.append(Q(user_id__contains=token))
            contents.append(Q(content__contains=token))
            titles.append(Q(title__contains=token))
            names.append(Q(name__contains=token))

        if ids: ids = reduce(Q.__or__, ids)
        if titles: titles = reduce(Q.__or__, titles)
        if contents: contents = reduce(Q.__or__, contents)
        if names: names = reduce(Q.__or__, names)

        Qs = filter(None, [ids, titles, contents, names])
        if Qs:
            return reduce(Q.__or__, Qs)
        else:
            return None

    @classmethod
    def get_list(self, board_id, page=0, per_page=20, q=None):
        s = page * per_page
        e = s + per_page
        board_model = Article.eval(board_id)
        all_articles = board_model.objects.all().order_by('-reg_date')
        if q:
            query = self._get_query_from_natual_language(q) 
            if query:
                matched_articles = board_model.objects.filter(query)
            else:
                matched_articles = all_articles
        else:
            matched_articles = all_articles
        
        total_articles = all_articles.count()
        total_matched_articles = matched_articles.count()
        paged_articles = matched_articles[s:e]
        
        listinfo = {'board_id': board_id,
                    'board_title': Board.get(board_id)['title'],
                    'page': page,
                    'per_page': per_page,
                    'total_pages': (total_matched_articles / per_page) + 1,
                    'q': q,
                    'total_matched_articles': total_matched_articles,
                    'total_articles': total_articles}        
        
        packed_articles = map(lambda article: Article.pack(article, board_id),
                              paged_articles)
        return listinfo, packed_articles
    
    @classmethod
    def post(self, board_id, user_id, title, message):
        article_model = Article.eval(board_id)        
        max_idx = article_model.objects.all().aggregate(Max('idx'))['idx__max']
        if not max_idx:
            max_idx = 0
        user = models.Member.objects.get(id=user_id)
        
        if board_id == 'board_anonymous':
            article_user_id = ""
            article_user_name = ""
            article_user_email = ""
        else:
            article_user_id = user_id
            article_user_name = user.name
            article_user_email = user.email
            
        article = article_model(idx=max_idx + 1, user_id=article_user_id,
                                name=article_user_name,
                                email=article_user_email, category="",
                                notice_deadline=datetime.datetime.min,
                                reg_date=datetime.datetime.now(),
                                count=0, title=title, content=message,
                                thread="A", comment=0)
        article.save()

class User(object):
    OPEN_FLAG = ((0, 'email'),
                 (1, 'homepage'),
                 (2, 'birthday'),
                 #(3, 'homeaddress'),
                 #(4, 'homephone'),
                 (5, 'mobile'),
                 #(6, 'jobcategory'),
                 (7, 'messenger'),
                 (8, 'introduce'),
                 #(9, 'department'),
                 #(10, 'workaddress'),
                 #(11, 'workphone'),
                 ) 
    
    @classmethod
    def pack(self, user_model):
        if user_model.birthday:
            birthday = user_model.birthday.isoformat()
        else:
            birthday = ""
        packed_user = {'id': user_model.id,
                       'name': user_model.name,
                       'entrance_year': user_model.id_number,
                       'img_url': self.get_img_url(user_model.id),
                       'mobile': user_model.cell_phone,
                       'homepage': user_model.homepage,
                       'birthday': birthday,
                       'email': user_model.email,
                       'introduce': user_model.introduce,
                       'messenger': user_model.messenger}
        
        # mask unopened informations 
        for i, field in self.OPEN_FLAG:
            if not (user_model.open_close & (2 ^ i)):
                packed_user[field] = None

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
    
    @classmethod
    def get_cafe(self, user_id):
        user = models.Member.objects.get(id=user_id)
        return user.cafe_name.split(',')

    @classmethod
    def search(self, q):
        years, ids, names = [], [], []
        re_entrance_year = re.compile(r"(\d+)")
        re_id = re.compile(r"(\w+)")

        # simple natural language processing
        for token in q.split():
            if re_entrance_year.match(token):
                years.append(token)
            elif re_id.match(token):
                ids.append(token)
            else:
                names.append(token)
        
        # make result
        Qs = []
        if years:
            Qs.append(reduce(Q.__or__, map(lambda x: Q(id_number=x), years)))
        if ids:
            Qs.append(reduce(Q.__or__, map(lambda x: Q(id__contains=x), ids)))
        if names:
            Qs.append(reduce(Q.__or__, map(lambda x: Q(name__contains=x), names)))
        if Qs:
            users = models.Member.objects.filter(reduce(Q.__and__, Qs))[:300]
            if users:
                return map(self.pack, users)
            else:
                raise Exception("No matching")
        else:
            raise Exception("No Query")
        
class Token(object):
    @classmethod
    def get_user_id(self, oauth_token):
        return OauthToken.objects.get(key=oauth_token).user
    
class Favorite(object):
    @classmethod
    def pack(self, favorite_model):
        packed_favorite = {'no': favorite_model.no,
                           'priority': favorite_model.priority,
                           'board_id': favorite_model.tablename}
        return packed_favorite
    
    @classmethod
    def get_by_user(self, user_id):
        favorites = models.Favorite.objects.filter(user_id=user_id)\
                                           .order_by('priority')
        return map(self.pack, favorites)

class Cafe(object):
    @classmethod
    def get_boards(self, cafe_id):
        cafe = models.CafeInfo.objects.get(cafe_name=cafe_id)
        return cafe.board_list.split(',') + cafe.photo_board_list.split(',')
        
    @classmethod
    def get_members(self, cafe_id):
        cafe = models.CafeInfo.objects.get(cafe_name=cafe_id)
        return cafe.member_list.split(',')
