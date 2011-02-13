# -*- coding: utf-8 -*-
from apiprj.api1_app import models
from apiprj.api1_app import modelwrap
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """삭제된 글에 남아있는 코멘트를 삭제함."""

    def handle(self, *args, **options):
        def comments(buf):
            return ((buf.startswith('Board') or buf.startswith('Photo')) and
                    (buf not in ('Photoinfo', 'Boardinfo')))
            
        def get_db_table(buf):
            return eval("models.%s._meta.db_table"%buf)
        
        board_ids = map(get_db_table, filter(comments , dir(models)))
        
        for board_id in board_ids:
            Comment = modelwrap.Comment.eval(board_id)
            Article = modelwrap.Article.eval(board_id)
            for comment in Comment.objects.all():
                if Article.objects.filter(id=comment.idx).count() == 0:
                    comment.delete()
        
