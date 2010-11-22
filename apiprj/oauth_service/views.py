from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from utils import oauth_required
import utils
import oauth2 as oauth

@oauth_required 
def request_token(request):
    consumer_key = request.REQUEST['oauth_consumer_key']
    callback = request.REQUEST['oauth_callback']
    token = utils.new_request_token(consumer_key, callback)
    return HttpResponse(token.to_string())


    # TODO: make and fetch real token here!!!
    #req_token_key = "request_token_key"
    #req_token_secret = "request_token_secret"
    #request_token = oauth.Token(key=req_token_key, secret=req_token_secret)
    #request_token.set_callback("http://call.back")

@csrf_exempt
@oauth_required 
def access_token(request):
    # TODO: need to verify verifier
    # TODO: make and fetch real token here
    access_token_key = "access_token_key"
    access_token_secret = "access_token_secret"
    access_token = oauth.Token(key=access_token_key, secret=access_token_key)
    return HttpResponse(access_token.to_string())

def authorize(request):
    ret = ""
    return HttpResponse(ret)

