#! -*- coding: utf-8 -*-
from apiprj.api1_app import models
from apiprj.api1_app import modelwrap
import datetime, random
from django.core.management.base import BaseCommand
from django.db.models import Q

def ask_continue(msg="Continue? (y/n) "):
    answer = ''
    while answer.lower() not in ('y', 'n'):
        answer = raw_input(msg)
    if answer.lower() == 'n':
        return False
    return True

def shuffle_str(buf):
    buf_list = [b for b in buf if b != u'<']
    random.shuffle(buf_list)
    return "".join(buf_list)

class Command(BaseCommand):
    """"""
    args = 'TODO: fill here'
    help = u"실제 데이터베이스의 내용을 지우고 변경해서 fixture를 생성할 수 있을만큼의 분량만 남김."
    
    def handle(self, *args, **options):
        del_msg_format = "%s\n%d items will be DELETED."
        
        # organize users
        users = ['gochi', 'jeppy', 'reset', 'unikth']
        q = reduce(Q.__or__ , (Q(id=user) for user in users))
        members = models.Member.objects.exclude(q)

        print del_msg_format % (members, members.count())
        if ask_continue(): 
            members.delete()

        # reset user             
        members = models.Member.objects.all()
        for member in members:
            member.student_id = int(str(member.student_id)[:4])
            member.email = member.id + '@caucse.net'
            member.cell_phone = '123-4567-8900'
            member.home_phone = '000-0000-0000'
            member.home_addr_1 = 'somewhere'
            member.home_addr_2 = 'over the rainbow'
            member.job_addr_1 = 'foo'
            member.job_addr_2 = 'bar'
            member.save()
            

        # organize boards            
        boards = ['board_alumni99', 'board_part_jungtong', 'board_part_plan',
                  'board_freeboard', 'board_anonymous', 'board_csesa']
        q = reduce(Q.__or__, (Q(tablename=board) for board in boards))
        boardinfos = models.Boardinfo.objects.exclude(q)
               
        print del_msg_format % (boardinfos, boardinfos.count())
        if ask_continue():
            for boardinfo in boardinfos:
                Board = modelwrap.Article.eval(boardinfo.tablename)
                Comment = modelwrap.Comment.eval(boardinfo.tablename)
                
                Board.objects.all().delete()
                Comment.objects.all().delete()
                boardinfo.delete()
                
        # organize photos
        photos = ['photo_alumni99', 'photo_part_jungtong', 'photo_part_plan',
                  'photo_memory', 'photo_info_memory', 'photo_info_02']
        q = reduce(Q.__or__, (Q(tablename=photo) for photo in photos))
        photoinfos = models.Photoinfo.objects.exclude(q)
        
        print del_msg_format % (photoinfos, photoinfos.count())
        if ask_continue():
            for photoinfo in photoinfos:
                Board = modelwrap.Article.eval(photoinfo.tablename)
                Comment = modelwrap.Comment.eval(photoinfo.tablename)
                
                Board.objects.all().delete()
                Comment.objects.all().delete()
                photoinfo.delete()
        
        # organize remain contents
        boards = boards + photos
        boards.remove('board_anonymous')
        q = reduce(Q.__or__, (Q(user_id=user) for user in users))
        for board in boards:
            Board = modelwrap.Article.eval(board)
            Comment = modelwrap.Comment.eval(board)
            for article in Board.objects.all():
                if (article.user_id in users) and (article.id % 20 == 0) :
                    for c in Comment.objects.filter(idx=article.id):
                        if c.user_id in users:
                            c.content = shuffle_str(c.content)
                            c.save()
                        else:
                            c.delete()
                    article.email = article.user_id + "@caucse.net"
                    article.notice_deadline = datetime.datetime.min
                    article.content = shuffle_str(article.content)
                    article.ip = '0.0.0.0'
                    article.save()
                    
                else:
                    Comment.objects.filter(idx=article.id).delete()
                    article.delete()
        
        # organize anonymous board
        Board = modelwrap.Article.eval('board_anonymous')
        for article in Board.objects.all():
            if article.id % 600 != 0:
                article.delete()
            else:
                article.content = shuffle_str(article.content)
                article.notice_deadline = datetime.datetime.min
                article.user_id = 'anonymous'
                article.email = 'anonymous'
                article.ip = '0.0.0.0'
                article.save()
        
        # organize cafeinfo
        for cafe in models.CafeInfo.objects.all():
            members = cafe.member_list.split(',')
            intersection = list(set(members).intersection(set(users)))
            if intersection:
                cafe.member_list = ",".join(intersection)
                cafe.save()
            else:
                cafe.delete()
        
        # organize favorite
        for favorite in models.Favorite.objects.all():
            if favorite.user_id not in users:
                favorite.delete()


        
        
