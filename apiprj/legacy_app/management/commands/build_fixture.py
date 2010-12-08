#! -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db.models import Q
from apiprj.legacy_app import models
from apiprj.api1_app import modelwrap

def ask_continue(msg="Continue? (y/n) "):
    answer = ''
    while answer.lower() not in ('y', 'n'):
        answer = raw_input(msg)
    if answer.lower() == 'n':
        return False
    return True

class Command(BaseCommand):
    args = 'TODO: fill here'
    help = 'TODO: fill here'
    
    def handle(self, *args, **options):
        del_msg_format = "%s\n%d items will be DELETED."
        
        # organize users
        users = ['gochi', 'jeppy', 'reset', 'unikth', 'napier', 'loslch',
                 'anoymity', 'sakurats', 'anjae83', 'hipbrain', 'ageratum',
                 'admin', 'perkytina']
        q = reduce(Q.__or__ , (Q(id=user) for user in users))
        members = models.Member.objects.exclude(q)

        print del_msg_format % (members, members.count())
        if ask_continue(): 
            members.delete()

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
