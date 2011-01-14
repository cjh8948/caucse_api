#! -*- coding: utf-8 -*-
from apiprj.api1_app import models
from django.core.management.base import BaseCommand

model_template = """\
class %(title)s(%(class)s):
    class Meta:
        db_table = u'%(tablename)s'"""

class Command(BaseCommand):
    def handle(self, *args, **options):
        def to_title(board):
            return board.replace("_", " ").title().replace(' ', '')
        def to_cmt(board):
            if board.startswith("board"):
                return "comment" + board[len('board'):]
            elif board.startswith("photo"):
                return "memo" + board[len('board'):]
        def memo_or_cmt(board):
            if board.startswith('board'):
                return "AbstractComment"
            else:
                return "AbstractMemo"
        
        boardinfos = models.Boardinfo.objects.all().order_by('tablename')
        photoinfos = models.Photoinfo.objects.all().order_by('tablename')
        boards = [boardinfo.tablename for boardinfo in boardinfos]
        photos = [photoinfo.tablename for photoinfo in photoinfos]
        
        for board in boards + photos:
            print "\n# auto generated for board %s" % board
            print model_template % {'title': to_title(board),
                                    'class':'AbstractBoard',
                                    'tablename': board}
            
            print model_template % {'title': to_title(to_cmt(board)),
                                    'class': memo_or_cmt(board),
                                    'tablename': to_cmt(board)}