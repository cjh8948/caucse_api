from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from urllib import urlencode
from utils import new_request_token, mysql_password
from utils.decorators import oauth_verify
from apiprj.api1_app.models import Member
from models import Token

@oauth_verify 
def request_token(request):
    consumer_key = request.REQUEST['oauth_consumer_key']
    callback = request.REQUEST['oauth_callback']
    token = new_request_token(consumer_key, callback)
    return HttpResponse(token.to_string())

@csrf_exempt
@oauth_verify 
def access_token(request):
    # need to verify verifier
    request_token = request.REQUEST['oauth_token']
    token = Token.objects.get(key=request_token)
    verifier = request.REQUEST['oauth_verifier']
    if token.type != 'R' or token.verifier != verifier:
        raise Exception
    
    # make and fetch real token here
    token.promote_to_access()
    access_token = token.to_oauth()
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

        # check user_id, password
        member = Member.objects.get(id=user_id) 
        if member.password != mysql_password(password):
            raise Exception("wrong password")

        # make verifier 
        token = Token.objects.get(key=oauth_token)
        token.new_verifier(user_id)
        oauth_token = token.to_oauth()

        # callback processing
        if token.callback == "oob": # pin processing
            params = {'verifier': token.verifier}
            return render_to_response('auth_verifier.html', params)
        else:
            params = {'oauth_token': token.key,
                      'oauth_verifier': token.verifier}
            callback_url = token.callback + "?" + urlencode(params)
            return HttpResponseRedirect(callback_url)