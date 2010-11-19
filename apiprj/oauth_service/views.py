from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api1.models import Member
from models import *
import utils
import oauth2 as oauth
 
def request_token(request):
    server = utils.AuthServer()
    oauth_request = server.conv_oauthrequest(request)

    # TODO: get consumer from DB
    consumer = oauth.Consumer(oauth_request['oauth_consumer_key'], 
                              'consumer_secret')
    params = server.verify_request(oauth_request, consumer, None)

    # TODO: make and fetch real token here!!!
    req_token_key = "request_token_key"
    req_token_secret = "request_token_secret"
    request_token = oauth.Token(key=req_token_key, secret=req_token_secret)

    return HttpResponse(request_token.to_string())

@csrf_exempt
def access_token(request):
    server = utils.AuthServer()
    oauth_request = server.conv_oauthrequest(request)

    # TODO: get real consumer, request token from DB
    consumer = oauth.Consumer(oauth_request['oauth_consumer_key'],
                              'consumer_secret')
    request_token = oauth.Token(oauth_request['oauth_token'],
                                'request_token_secret')
    params = server.verify_request(oauth_request, consumer, request_token)

    # TODO: need to verify verifier

    # TODO: make and fetch real token here
    access_token_key = "access_token_key"
    access_token_secret = "access_token_secret"
    access_token = oauth.Token(key=access_token_key, secret=access_token_key)
    return HttpResponse(access_token.to_string())

def authorize(request):
    ret = ""
    return HttpResponse(ret)

