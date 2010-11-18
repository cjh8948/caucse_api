from django.http import HttpResponse
from api1.models import Member
from models import *

def request_token(request):
    print request.GET['oauth_consumer_key']
    ret = "oauth_token=foo&oauth_token_secret=bar"
    return HttpResponse(ret)

def access_token(request):
    ret = ""
    return HttpResponse(ret)

def authorize(request):
    ret = ""
    return HttpResponse(ret)

