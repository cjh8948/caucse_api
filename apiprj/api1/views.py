from django.http import HttpResponse
from django.core import serializers
from django.utils.simplejson import dumps

import modelwrap 

from models import *
import datetime

# TODO: should separate logic from view

def articles_show(request):
    board_id = request.GET['board_id']
    article_id = int(request.GET['article_id'])
    article = modelwrap.get_article(board_id, article_id)
    ret = dumps(article, ensure_ascii=False) 
    return HttpResponse(ret)
    
def users_show(request):
    id = request.GET['user_id']
    member = Member.objects.get(id=id)
    ret = serializers.serialize('json', [member], ensure_ascii=False)
    return HttpResponse(ret)
    
def users_lookup(request):
    id_list = request.GET['user_id'].split(',')
    members = [Member.objects.get(id=id) for id in id_list]
    ret = serializers.serialize('json', members, ensure_ascii=False)
    return HttpResponse(ret)
 
def boards_lookup(request):
    board_list = request.GET['board_id'].split(',')
    boards = map(modelwrap.get_board, board_list)
    ret = dumps(boards, ensure_ascii=False)
    return HttpResponse(ret)

def articles_list(request):
    page = 0
    per_page = 20
    
    # get request parameter 
    board_id = request.GET['board_id']
    if request.GET.has_key('page'):
        page = int(request.GET['page'])
    if request.GET.has_key('per_page'):
        per_page = int(request.GET['per_page'])

    # make json object to return
    ret_item = {'option': {'board_id': board_id,
                           'page': page,
                           'per_page': per_page},
                'articles': modelwrap.get_articles(board_id, page, per_page)}
    ret = dumps(ret_item, ensure_ascii=False)

    return HttpResponse(ret)
