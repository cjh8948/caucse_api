from django.http import HttpResponse
from api1.models import Member
from models import *
import utils
import oauth2 as oauth
 
def request_token(request):
    server = utils.AuthServer()
    request = server.conv_oauthrequest(request)

    # TODO: get consumer from DB
    consumer = oauth.Consumer(request['oauth_consumer_key'], 'consumer_secret')
    params = server.verify_request(request, consumer, None)

    # TODO: make and fetch real token here!!!
    req_token_key = "request_token_key"
    req_token_secret = "request_token_secret"
    request_token = oauth.Token(key=req_token_key, secret=req_token_secret)

    return HttpResponse(request_token.to_string())

def access_token(request):
    ret = "hmm.."
    return HttpResponse(ret)

def authorize(request):
    ret = ""
    return HttpResponse(ret)

