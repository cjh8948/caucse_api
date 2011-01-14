#-*- coding:utf-8 -*-
from apiprj.api1_app.utils.decorators import api_exception
from apiprj.exceptions import RequiredParameterDoesNotExist
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import (HttpResponse, HttpResponseRedirect,
                         HttpResponseBadRequest, HttpResponseForbidden)
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from models import Token
from urllib import urlencode
from urlparse import parse_qsl, urlparse, urlunparse 
from utils.decorators import oauth_verify

@api_exception
@oauth_verify 
def request_token(request, oauth_params):
    """This API grants request_token
    
    * resource: 'oauth/request_token'
    ** method: oauth
    ** mandatory parameter: see [[OauthAuthentication]]"""
    try:
        consumer_key = oauth_params['oauth_consumer_key']
        callback = oauth_params['oauth_callback']
    except KeyError:
        return HttpResponseBadRequest()
    token = Token.new_request_token(consumer_key, callback)
    return HttpResponse(token.to_oauth().to_string())

@csrf_exempt
@api_exception
@oauth_verify 
def access_token(request, oauth_params):
    """This API grants access_token
    
    * resource: 'oauth/access_token'
    ** method: oauth
    ** mandatory parameter: see [[OauthAuthentication]]"""    
    # need to verify verifier
    try:
        request_token = oauth_params['oauth_token']
        verifier = oauth_params['oauth_verifier']
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
        try:
            oauth_token = request.REQUEST['oauth_token']
        except KeyError as e:
            raise RequiredParameterDoesNotExist(str(e))
         
        try:
            token = Token.objects.get(key=oauth_token)
        except ObjectDoesNotExist:
            return HttpResponseForbidden()
        params = {'oauth_token' : oauth_token, 'consumer' : token.consumer}
        return render_to_response('oauth/auth_form.tpl', params,
                                  context_instance=RequestContext(request))

    elif request.method == "POST":
        if request.user.is_authenticated():
            user_id = request.user.username
        else:
            # check user_id, password
            user_id = request.REQUEST['user_id']
            password = request.REQUEST['password']
            oauth_token = request.REQUEST['oauth_token']
            user = authenticate(username=user_id, password=password)
            if user:
                if user.is_active:
                    login(request, user)
            else:
                token = Token.objects.get(key=oauth_token)
                message = u"사용자 아이디와 비밀번호가 일치하지 않습니다."
                params = {'oauth_token' : oauth_token,
                          'consumer' : token.consumer,
                          'message': message}
                return render_to_response('oauth/auth_form.tpl', params,
                                          context_instance=RequestContext(request))
                    
        # make verifier 
        oauth_token = request.REQUEST['oauth_token']
        token = Token.objects.get(key=oauth_token)
        token.new_verifier(user_id)
        oauth_token = token.to_oauth()

        # callback processing
        if token.callback == "oob": # pin processing
            params = {'verifier': token.verifier}
            return render_to_response('oauth/auth_verifier.tpl', params,
                                      context_instance=RequestContext(request))
        else:
            params = {'oauth_token': token.key,
                      'oauth_verifier': token.verifier}
            parsed_callback = list(urlparse(token.callback))
            params.update(dict(parse_qsl(parsed_callback[4])))
            parsed_callback[4] = urlencode(params)
            callback_url = urlunparse(parsed_callback)
            return HttpResponseRedirect(callback_url)
