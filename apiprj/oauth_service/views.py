from django.http import HttpResponse
from api1.models import Member
from models import *
import utils
  
def request_token(request):
    oauth_server, oauth_request = utils.initialize_server_request(request)
    # TODO: make token here!!!
    token = "psuedo token"
    return HttpResponse(token)

def access_token(request):
    ret = ""
    return HttpResponse(ret)

def authorize(request):
    ret = ""
    return HttpResponse(ret)

