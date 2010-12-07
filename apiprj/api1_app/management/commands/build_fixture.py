#! -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db.models import Q
from apiprj.api1_app import models
from apiprj.api1_app import modelwrap

def ask_continue(msg):
    answer = ''
    while answer.lower() not in ('y', 'n'):
        answer = raw_input(msg)
    if answer.lower() == 'n':
        return False
    return True

class Command(BaseCommand):
    args = 'args str'
    help = 'help str'
    

    
    def handle(self, *args, **options):
        msg_format = "%s\n%d items will be DELETED. continue?(y/n) "
        
        # organize users
        users = ['gochi', 'jeppy', 'reset', 'unikth', 'napier', 'loslch',
                 'anoymity', 'sakurats', 'anjae83', 'hipbrain', 'ageratum',
                 'admin', 'perkytina']
        q = reduce(Q.__or__ , (Q(id=user) for user in users))
        members = models.Member.objects.exclude(q)
        msg = msg_format % (members, members.count())
        if ask_continue(msg): 
            members.delete()

        # organize boards            
        boards = ['board_alumni99', 'board_part_jungtong', 'board_part_plan',
                  'board_freeboard', 'board_anonymous', 'board_csesa']
        q = reduce(Q.__or__, (Q(tablename=board) for board in boards))
        boardinfos = models.Boardinfo.objects.exclude(q)
        msg = msg_format % (boardinfos, boardinfos.count())
        if ask_continue(msg):
            boardinfos.delete()




