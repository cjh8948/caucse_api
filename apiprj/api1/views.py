from django.http import HttpResponse
from django.core import serializers
from django.utils.simplejson import dumps

from models import *
import datetime

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

    # lookup board information from board_id param.
    boardinfo = []
    for tablename in board_list:
        if tablename.startswith('board'):
            boardinfo.append(Boardinfo.objects.get(tablename=tablename))
        elif tablename.startswith('photo'):
            boardinfo.append(Photoinfo.objects.get(tablename=tablename))

    # compose data to make json
    boards = []
    for board in boardinfo:
        board_dict = {}
        classname = board.tablename.title().replace('_','')
        board_model = eval(classname)
        day_ago = datetime.datetime.today() - datetime.timedelta(days=1)
        
        board_dict['board_id'] = board.tablename
        board_dict['title'] = board.title
        board_dict['description'] = board.description
        board_dict['admin'] = board.admin_id
        board_dict['count'] = board_model.objects.count()
        board_dict['count_24h_ago'] = board_model.objects\
                                                 .filter(reg_date__gt=day_ago)\
                                                 .count()
        boards.append(board_dict)

    # return json object
    ret = dumps(boards, ensure_ascii=False)
    return HttpResponse(ret)

