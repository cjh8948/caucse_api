from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from utils import oauth_verify
import utils
import oauth2 as oauth
import models
from api1_app.models import Member
import urllib

@oauth_verify 
def request_token(request):
    consumer_key = request.REQUEST['oauth_consumer_key']
    callback = request.REQUEST['oauth_callback']
    token = utils.new_request_token(consumer_key, callback)
    return HttpResponse(token.to_string())

@csrf_exempt
@oauth_verify 
def access_token(request):
    # need to verify verifier
    request_token = request.REQUEST['oauth_token']
    token = models.Token.objects.get(key=request_token)
    verifier = request.REQUEST['oauth_verifier']
    if token.type != 'R' or token.verifier != verifier:
        raise Exception
    
    # make and fetch real token here
    token.promote_to_access()
    access_token = token.to_oauth_token()
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
            raise Exception("wrong password")

        # make verifier 
        token = models.Token.objects.get(key=oauth_token)
        token.user = user_id
        token.new_verifier()
        oauth_token = token.to_oauth_token()

        # callback processing
        if token.callback == "oob": # pin processing
            params = {'verifier': token.verifier}
            return render_to_response('auth_verifier.html', params)
        else:
            params = {'oauth_token': token.key,
                      'oauth_verifier': token.verifier}
            callback_url = token.callback + "?" + urllib.urlencode(params)
            return HttpResponseRedirect(callback_url)
