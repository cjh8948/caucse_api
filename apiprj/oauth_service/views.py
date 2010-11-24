from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from utils import oauth_required
import utils
import oauth2 as oauth
import models
from api1.models import Member

@oauth_required 
def request_token(request):
    consumer_key = request.REQUEST['oauth_consumer_key']
    callback = request.REQUEST['oauth_callback']
    token = utils.new_request_token(consumer_key, callback)
    return HttpResponse(token.to_string())

@csrf_exempt
@oauth_required 
def access_token(request):
    # TODO: need to verify verifier
    # TODO: make and fetch real token here
    access_token_key = "access_token_key"
    access_token_secret = "access_token_secret"
    access_token = oauth.Token(key=access_token_key, secret=access_token_key)
    return HttpResponse(access_token.to_string())

@csrf_exempt
def authorize(request):
    if request.method == "GET":
        params = {'oauth_token' : request.REQUEST['oauth_token']}
        return render_to_response('auth_form.html', params)

    elif request.method == "POST":
        user_id = request.REQUEST['user_id']
        password = request.REQUEST['password']
        oauth_token = request.REQUEST['oauth_token']

        # check password
        member = Member.objects.get(id=user_id) 
        if member.password != utils.mysql_password(password):
            raise Exception

        # make verifier 
        token = models.Token.objects.get(key=oauth_token)
        token.new_verifier()
        oauth_token = token.to_oauth_token()

        # callback processing
        if token.callback == "oob": # pin processing
            params = {'verifier': token.verifier}
            return render_to_response('auth_verifier.html', params)
        else:
            # TODO: redirect to callback url
            return HttpResponse("not implemented yet")

