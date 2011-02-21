﻿#-*-coding:utf-8-*-
"""
"""
from apiprj.api1_app import models
from apiprj.exceptions import (
    DatabaseTableDoesNotExist,
    PermissionDenied,
    NoMatchingResult
)
from apiprj.oauth_app.models import Token as OauthToken
from apiprj.settings import USER_IMG_PATH, USER_IMG_PREFIX
from django.db.models.aggregates import Max
from django.db.models import Q, ObjectDoesNotExist
import os, datetime, re

def strip_quotes(buf):
    return buf.replace(r'\"', '"').replace(r"\'", "'")

def check_permission(board_id, user_id, permission_digit):
    try:
        if board_id.startswith('board_'):
            boardinfo = models.Boardinfo.objects.get(tablename=board_id)
        elif board_id.startswith('photo_'):
            boardinfo = models.Photoinfo.objects.get(tablename=board_id)
    except ObjectDoesNotExist as e:
        raise DatabaseTableDoesNotExist(e)

    if not boardinfo.check_permission(permission_digit, user_id):
        raise PermissionDenied(user_id)

class Board(object):
    @classmethod
    def pack(self, boardinfo_model, count=None, count24h=None):
        packed_board = {
            'board_id': boardinfo_model.tablename,
            'title': strip_quotes(boardinfo_model.title),
            'description': strip_quotes(boardinfo_model.description),
            'admin': boardinfo_model.admin_id,
            'count': count,
            'count24h': count24h
        }
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
        # 일반 게시판의 경우 board_* 의 커멘트 table은 comment_*
        if board_id.startswith('board'):
            prefix = "Comment"
        # 사진 게시판의 경우 photo_* 의 커멘트 table은 memo_*
        elif board_id.startswith('photo'):
            prefix = "Memo"
        comment_classname = prefix + board_id.title().replace('_', '')[5:]
        if comment_classname not in dir(models):
            raise DatabaseTableDoesNotExist(comment_classname)
        return eval("models." + comment_classname)

    @classmethod
    def pack(self, cmt_model, board_id):
        author = {
            'name': cmt_model.name,
            'id': cmt_model.user_id,
            'img_url': User.get_img_url(cmt_model.user_id)
        }

        packed_cmt = {
            'board_id': board_id,
            'id': cmt_model.id,
            'content': strip_quotes(cmt_model.content),
            'reg_date': cmt_model.reg_date.isoformat(),
            'author': author
        }

        return packed_cmt

    @classmethod
    def get(self, board_id, article_id):
        comment_model = Comment.eval(board_id)
        comments = comment_model.objects.filter(idx=article_id)
        return map(lambda cmt: Comment.pack(cmt, board_id), comments)

    @classmethod
    def post(self, board_id, article_id, user_id, content):
        check_permission(board_id, user_id, models.Boardinfo.COMMENT_DIGIT)

        # check if article exists
        article_model = Article.eval(board_id)
        article = article_model.objects.get(id=article_id)

        # add comment
        comment_model = Comment.eval(board_id)
        user_name = models.Member.objects.get(id=user_id).name
        cmt = comment_model(
            idx=article_id,
            user_id=user_id,
            name=user_name,
            content=content,
            reg_date=datetime.datetime.today()
        )
        cmt.save()

        # inc article.comment
        article.inc_comment_count()
        article.save()

        return self.pack(cmt, board_id)

    @classmethod
    def delete(self, board_id, comment_id, user_id):
        check_permission(board_id, user_id, models.Boardinfo.COMMENT_DIGIT)

        comment_model = Comment.eval(board_id).objects.get(id=comment_id)
        if comment_model.user_id == user_id:
            # get article model
            article_model = Article.eval(board_id)
            article = article_model.objects.get(id=comment_model.idx)

            # delete comment_model
            comment_model.delete()

            # dec article_model.comment
            article.dec_comment_count()
            article.save()

        else:
            raise PermissionDenied(user_id)

class Article(object):
    @classmethod
    def eval(self, board_id):
        board_classname = board_id.title().replace('_', '')
        if board_classname not in dir(models):
            raise DatabaseTableDoesNotExist(board_classname)
        return eval("models." + board_classname)

    @classmethod
    def pack(self, article_model, board_id, comments=[]):
        author = {
            'name': article_model.name,
            'id': article_model.user_id,
            'img_url': User.get_img_url(article_model.user_id)
        }

        packed_article = {
            'board_id': board_id,
            'id': article_model.id,
            'author': author,
            'title': strip_quotes(article_model.title),
            'hits': article_model.count,
            'reg_date': article_model.reg_date.isoformat(),
            'content': strip_quotes(article_model.content),
            'file': article_model.file_name,
            'comments': comments,
            'total_comments': article_model.comment
        }

        return packed_article

    @classmethod
    def get(self, board_id, article_id, user_id):
        check_permission(board_id, user_id, models.Boardinfo.VIEW_DIGIT)
        board_model = Article.eval(board_id)
        article_model = board_model.objects.get(id=article_id)
        comments = Comment.get(board_id, article_id)
        article = Article.pack(article_model, board_id, comments)
        
        if user_id != article_model.user_id: 
            article_model.inc_hit_count()
            article_model.save()  
              
        return article

    @classmethod
    def delete(self, board_id, article_id, user_id):
        board_model = Article.eval(board_id)
        article_model = board_model.objects.get(id=article_id)
        if user_id != article_model.user_id:
            raise PermissionDenied(user_id)
        article_model.delete()

    @classmethod
    def _build_query(self, q):
        q = q.strip()
        if len(q) < 2 : return None

        return (
            Q(content__icontains=q) |
            Q(title__icontains=q) |
            Q(user_id__icontains=q) |
            Q(name__icontains=q)
        )

    @classmethod
    def get_list(self, board_id, user_id, page=0, per_page=20, q=""):
        # check permission
        check_permission(board_id, user_id, models.Boardinfo.LIST_DIGIT)

        s = page * per_page
        e = s + per_page
        q = q.strip()
        board_model = Article.eval(board_id)
        articles = board_model.objects.all()
        total_articles = articles.count()

        query = self._build_query(q)
        if query:
            articles = articles.filter(query)

        total_matched_articles = articles.count()
        paged_articles = articles.order_by('-reg_date')[s:e]

        listinfo = {
            'board_id': board_id,
            'board_title': Board.get(board_id)['title'],
            'page': page,
            'per_page': per_page,
            'total_pages': (total_matched_articles / per_page),
            'total_matched_articles': total_matched_articles,
            'total_articles': total_articles,
            'q': q
        }

        packed_articles = map(lambda article: Article.pack(article, board_id),
                              paged_articles)
        return listinfo, packed_articles

    @classmethod
    def update(self, board_id, article_id, user_id, title, message):
        check_permission(board_id, user_id, models.Boardinfo.WRITE_DIGIT)

        article_model = Article.eval(board_id)
        article = article_model.objects.get(id=article_id)

        if article.user_id != user_id:
            raise PermissionDenied(user_id)

        article.title = title
        article.content = message

        if article.notice_deadline == None:
            article.notice_deadline = datetime.datetime.min

        article.save()
        return self.pack(article, board_id)


    @classmethod
    def post(self, board_id, user_id, title, message):
        check_permission(board_id, user_id, models.Boardinfo.WRITE_DIGIT)

        article_model = Article.eval(board_id)
        max_idx = article_model.objects.all().aggregate(Max('idx'))['idx__max']
        if not max_idx:
            max_idx = 0
        user = models.Member.objects.get(id=user_id)

        article = article_model(
            idx=max_idx + 1,
            user_id=user_id,
            name=user.name,
            email=user.email,
            category="",
            notice_deadline=datetime.datetime.min,
            reg_date=datetime.datetime.now(),
            count=0,
            title=title,
            content=message,
            thread="A",
            comment=0
        )
        article.save()
        return self.pack(article, board_id)

class User(object):
    OPEN_FLAG = (
        (0, 'email'),
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

        if user_model.id_number:
            entrance_year = 1900 + user_model.id_number
        else:
            entrance_year = None

        packed_user = {
            'id': user_model.id,
            'name': user_model.name,
            'entrance_year': entrance_year,
            'img_url': self.get_img_url(user_model.id),
            'mobile': user_model.cell_phone,
            'homepage': user_model.homepage,
            'birthday': birthday,
            'email': user_model.email,
            'introduce': strip_quotes(user_model.introduce),
            'messenger': user_model.messenger
        }

        # mask closed informations
        for i, field in self.OPEN_FLAG:
            if not (user_model.open_close & (2 ^ i)):
                packed_user[field] = None
        return packed_user

    @classmethod
    def get_img_url(self, user_id):
        img_path = os.path.join(USER_IMG_PATH, user_id)
        if type(img_path) is unicode:
            img_path = img_path.encode('utf-8')
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
        if user.cafe_name:
            return user.cafe_name.split(',')
        else:
            return []

    @classmethod
    def search(self, q):
        years, ids, names = [], [], []
        re_entrance_year = re.compile(r"(\d+)")
        re_id = re.compile(r"(\w+)")

        # simple natural language processing
        for token in q.split():
            if re_entrance_year.match(token):
                token = int(token)
                if token >= 1900:
                    token -= 1900
                elif token < 50:
                    token += 100
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
        users = models.Member.objects.filter(reduce(Q.__and__, Qs))[:300]
        if users:
            return map(self.pack, users)
        else:
            raise NoMatchingResult("No matching")

class Token(object):
    @classmethod
    def get_user_id(self, oauth_token):
        return OauthToken.objects.get(key=oauth_token).user

class Favorite(object):
    @classmethod
    def pack(self, favorite_model):
        packed_favorite = {
            'no': favorite_model.no,
            'priority': favorite_model.priority,
            'board_id': favorite_model.tablename
        }
        return packed_favorite

    @classmethod
    def get_by_user(self, user_id):
        favorites = models.Favorite.objects.filter(user_id=user_id)\
                                           .order_by('priority')
        return map(self.pack, favorites)

class Cafe(object):
    category = (
        u'N/A', # 0
        u'학생자치', # 1
        u'학회', # 2
        u'레저/스포츠', # 3
        u'인문사회', # 4
        u'문화예술', # 5
        u'친목모임', # 6        
        u'동문회' # 7      
    )

    @classmethod
    def get_boards(self, cafe_id):
        cafe = models.CafeInfo.objects.get(cafe_name=cafe_id)
        return cafe.board_list.split(',') + cafe.photo_board_list.split(',')

    @classmethod
    def get_members(self, cafe_id):
        cafe = models.CafeInfo.objects.get(cafe_name=cafe_id)
        return cafe.member_list.split(',')

    @classmethod
    def _build_query(self, q):
        q = q.strip()

        if len(q) < 1 : return None

        return (
            Q(cafe_nick__icontains=q) |
            Q(cafe_name__icontains=q)
        )

    @classmethod
    def get_list(self, q=""):
        q = q.strip()
        cafes = models.CafeInfo.objects.filter(is_hidden=0)
        total_cafes = cafes.count()

        query = self._build_query(q)
        if query:
            cafes = cafes.filter(query)
            
        cafes = cafes.order_by('no').order_by('section')

        total_matched_cafes = cafes.count()
        
        listinfo = {
            'total_matched_cafes': total_matched_cafes,
            'total_cafes': total_cafes,
            'q': q
        }

        packed_articles = map(Cafe.pack, cafes)
        return listinfo, packed_articles

    @classmethod
    def pack(self, cafe_model):
        board_list = cafe_model.board_list.split(',') + \
                     cafe_model.photo_board_list.split(',')

        packed_cafes = {
            'no': cafe_model.no,
            'cafe_id': cafe_model.cafe_name,
            'cafe_name': cafe_model.cafe_nick,
            'admin': cafe_model.adminid,
            'member_list': cafe_model.member_list.split(','),
            'board_list': board_list,
            'description': cafe_model.front_text,
            'category': self.category[cafe_model.section]
        }

        return packed_cafes
