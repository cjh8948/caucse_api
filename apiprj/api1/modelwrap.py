#!/usr/bin/python

import models
import datetime

class ModelnameError(Exception):pass

def eval_board(board_id):
    board_classname = board_id.title().replace('_','')
    if board_classname not in dir(models):
        raise ModelnameError
    return eval("models."+board_classname)

def eval_comment(board_id):
    comment_classname = "Comment"+board_id.title().replace('_','')[5:]
    if comment_classname not in dir(models):
        raise ModelnameError
    return eval("models."+comment_classname)

def pack_comment(cmt, board_id):
    packed_cmt = {'board_id': board_id, 
                  'id': cmt.id, 
                  'content': cmt.content,
                  'reg_date': cmt.reg_date.isoformat(),
                  'author': {'name': cmt.name, 
                             'id': cmt.user_id}}
    return packed_cmt

def pack_article(article, board_id, comments=[]):
    packed_article = {'board_id': board_id,
                      'id': article.id,
                      'author': {'name': article.name,
                                 'id': article.user_id},
                      'title': article.title,
                      'view_count': article.count,
                      'reg_date': article.reg_date.isoformat(),
                      'content': article.content,
                      'file': article.file_name,
                      'comments': comments}
    return packed_article

def get_comments(board_id, article_id):
    comment_model = eval_comment(board_id)
    comments = comment_model.objects.filter(idx=article_id)
    return map(lambda cmt: pack_comment(cmt, board_id), comments)

def get_article(board_id, article_id):
    board_model = eval_board(board_id)
    article_model = board_model.objects.get(id=article_id)
    comments = get_comments(board_id, article_id)
    article = pack_article(board_id, article_model, comments) 
    return article

