from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from urllib import urlencode
from utils import check_mysql_password
from utils.decorators import oauth_verify
from apiprj.api1_app.utils.decorators import api_exception
from apiprj.legacy_app.models import Member
from models import Token

@api_exception
@oauth_verify 
def request_token(request):
    """This API grants request_token
    
    * resource: 'oauth/request_token'
    ** method: oauth
    ** mandatory parameter: see [[OauthAuthentication]]"""    
    try:
        consumer_key = request.REQUEST['oauth_consumer_key']
        callback = request.REQUEST['oauth_callback']
    except KeyError:
        return HttpResponseBadRequest()
    token = Token.new_request_token(consumer_key, callback)
    return HttpResponse(token.to_oauth().to_string())

@csrf_exempt
@api_exception
@oauth_verify 
def access_token(request):
    """This API grants access_token
    
    * resource: 'oauth/access_token'
    ** method: oauth
    ** mandatory parameter: see [[OauthAuthentication]]"""    
    # need to verify verifier
    try:
        request_token = request.REQUEST['oauth_token']
        verifier = request.REQUEST['oauth_verifier']
    except KeyError:
        return HttpResponseBadRequest()

    try:
        token = Token.objects.get(key=request_token)
    except ObjectDoesNotExist:
        return HttpResponseBadRequest()
    
    if token.type != 'R' or token.verifier != verifier:
        return HttpResponseBadRequest()
    
    # make and fetch real token here
    token.promote_to_access()
    access_token = token.to_oauth()
    return HttpResponse(access_token.to_string())

@api_exception
@csrf_exempt
def authorize(request):
    """This API asks the user for granting the consumer access protected 
    resources. 
    
    * resource: 'oauth/access_token'
    ** method: GET
    ** mandatory parameter: see [[OauthAuthentication]]    
    
    * resource: 'oauth/access_token'
    ** method: POST
    ** mandatory parameter: see [[OauthAuthentication]]
    """
    if request.method == "GET":
        params = {'oauth_token' : request.REQUEST['oauth_token']}
        return render_to_response('auth_form.html', params)

    elif request.method == "POST":
        user_id = request.REQUEST['user_id']
        password = request.REQUEST['password']
        oauth_token = request.REQUEST['oauth_token']

        # check user_id, password
        member = Member.objects.get(id=user_id) 
        if not check_mysql_password(password, member.password):
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
