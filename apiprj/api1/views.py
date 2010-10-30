from django.http import HttpResponse
from django.core import serializers
from django.utils.simplejson import dumps

from models import Boardinfo, Member

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
 
def boards_list(request):
    boards = Boardinfo.objects.all()
    ret = serializers.serialize('json', boards, ensure_ascii=False)
    return HttpResponse(ret)

