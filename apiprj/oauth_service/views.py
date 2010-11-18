from django.http import HttpResponse
from api1.models import Member
from models import *
import oauth2 as oauth

def initialize_server_request(request):
    auth_header = {}
    if request.META.has_key('Authorization'):
        auth_header['Authorization'] = request.META['Authorization']
    elif request.META.has_key('HTTP_AUTHORIZATION'):
        auth_header['Authorization'] = request.META['HTTP_AUTHORIZATION']

    parameters = {}
    if request.method == "POST" and\
       request.META['CONTENT_TYPE'] == "applicaion/x-www-form-urlencoded":
        parameters = dict(request.REQUEST.items())

    query_string = request.META.get('QUREY_STRING','')
    oauth_request = oauth.Request.from_request(request.method,
                                               request.build_absolute_uri(),
                                               headers=auth_header,
                                               parameters=parameters,
                                               query_string=query_string)

    if oauth_request:
        oauth_server = oauth.Server()
        oauth_server.add_signature_method(oauth.SignatureMethod_HMAC_SHA1()) 
    else: 
        oauth_server = None
    
    return oauth_server, oauth_request
  
def request_token(request):
    oauth_server, oauth_request = initialize_server_request(request)
    # TODO: make token here!!!
    token = "psuedo token"
    return HttpResponse(token)

def access_token(request):
    ret = ""
    return HttpResponse(ret)

def authorize(request):
    ret = ""
    return HttpResponse(ret)

