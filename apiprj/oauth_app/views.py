#-*- coding:utf-8 -*-
from apiprj.api1_app.utils.decorators import api_exception
from apiprj.exceptions import RequiredParameterDoesNotExist, AuthError
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.http import (HttpResponse, HttpResponseRedirect,
                         HttpResponseBadRequest, HttpResponseForbidden)
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from models import Token, Consumer
from urllib import urlencode
from urlparse import parse_qsl, urlparse, urlunparse 
from utils.decorators import oauth_verify

@csrf_exempt
@api_exception
@oauth_verify 
def request_token(request, oauth_params):
    """
    **/oauth/request_token**

    3 legged 인증의 첫번째 단계. 리소스 프로바이더가 [1]_ 컨슈머 [2]_ 의 
    서명을 확인 후 request token을 반환
    
    다음 단계는 authorize 단계로, 컨슈머가 [2]_ 사용자 [3]_ 를 authorize 
    페이지로 보내어(리다이렉트 또는 url 제공) access token을 발급하도록 한다. 
    
    method
     * POST
     * oauth_signature required 
    
    oauth paramters
     * oauth_callback
     * oauth_consumer_key
     * oauth_nonce
     * oauth_signature_method
     * oauth_timestamp
     * oauth_version
    
    note
     * 동네API는 oauth_signature_method 로 HMAC-SHA1만을 지원한다.
     * 동네API는 oauth_version 1.0을 지원한다.
     * callback을 처리할 수 없는 클라이언트는 oauth_callback 값으로 "oob"(out-of-band)를 설정하면 PIN(개인 인증 번호) flow을 따를 수 있다.
    
    footnote
     .. [1] resource provider; 자원 제공자인 동네API를 의미
     .. [2] consumer; 동네API를 사용하는 것이 허가된 애플리케이션
     .. [3] user; 동네 회원. 컨슈머에게 패스워드를 알려주지 않는 대신, access token을 발급해주어서 보호된 자원을 컨슈머가 사용하도록 허가 또는 불허할 수 있다.
    
    """
    if request.method == "GET":
        raise AuthError("request method for 'request token' should be POST")
    
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
    """
    **/oauth/access_token**

    3 legged 인증의 세번째 단계. 리소스 프로바이더가 [1]_ 컨슈머 [2]_ 의 
    서명과 User [3]_ 가 리소스 프로바이더 [1]_ 로 부터 제공받은 Verifier를 
    확인 후 access token을 반환
    
    이 단계 이후부터 컨슈머 [2]_ 는 access token을 이용해서 protected 
    resource에 접근할 수 있다. 
    
    method
     * POST
     * oauth_signature required 
    
    oauth paramters
     * oauth_consumer_key
     * oauth_nonce
     * oauth_signature_method
     * oauth_timestamp
     * oauth_token
     * oauth_version
    
    note
     * 동네API는 oauth_signature_method 로 HMAC-SHA1만을 지원한다.
     * 동네API는 oauth_version 1.0을 지원한다.
    
    footnote
     .. [1] resource provider; 자원 제공자인 동네API를 의미
     .. [2] consumer; 동네API를 사용하는 것이 허가된 애플리케이션
     .. [3] user; 동네 회원. 컨슈머에게 패스워드를 알려주지 않는 대신, access token을 발급해주어서 보호된 자원을 컨슈머가 사용하도록 허가 또는 불허할 수 있다.
    
    """    
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
    r"""
    **/oauth/authorize**
    
    3 legged 인증의 두번째 단계. 첫번째 단계에서 획득한 request token를 가지고
    컨슈머가 보호된 자원에 접근할 수 있도록 access token을 발행할지 사용자에게 
    확인한다.
    
    GET method case
    ~~~~~~~~~~~~~~~
    사용자의 인증 정보(아이디/패스워드)를 포함, access token을 발행할지 여부를 
    물어보는 양식(form) 페이지를 보여준다. 
            
    parameters
        * oauth_token: request token key 
     
    POST method case
    ~~~~~~~~~~~~~~~~
    access token 발행 양식 페이지에서 사용자 및 컨슈머를 인증하고 첫번째 
    단계에서 획득한 callback url로 리다이렉트 한다. callback이 "oob"인 경우 
    PIN(개인 인증 번호)를 포함한 페이지를 보여준다.

    """
    if request.method == "POST":
        user_id = None
        if not request.user.is_authenticated():
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                if request.session.test_cookie_worked():
                    request.session.delete_test_cookie()   
                user_id = request.user.username
        else: 
            user_id = request.user.username
        
        if user_id:            
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
            
    # form is not valid or GET
    form = AuthenticationForm(request)
    try:
        oauth_token = request.REQUEST['oauth_token']
    except KeyError as e:
        raise RequiredParameterDoesNotExist(str(e))     
    try:
        token = Token.objects.get(key=oauth_token)
    except ObjectDoesNotExist:
        return HttpResponseForbidden()    
    params = {'oauth_token' : oauth_token, 'consumer' : token.consumer,
              'form': form}    
    return render_to_response('oauth/auth_form.tpl', params,
                              context_instance=RequestContext(request))

def index(request):
    return render_to_response('index.tpl',
                              context_instance=RequestContext(request))    

@login_required
def accounts_profile(request):
    user_id = request.user.username
    consumers = Consumer.objects.filter(user_id=user_id)
    tokens = Token.objects.filter(user=user_id).filter(type='A')
    params = {'consumers': consumers, 'tokens': tokens}
    return render_to_response('profile.tpl', params,
                              context_instance=RequestContext(request))    
    
def apistatus(request):
    consumers = Consumer.objects.annotate(num_tokens=Count('token'))\
                                .order_by('-num_tokens')
                                
    params = {'consumers' : consumers}
    
    return render_to_response('apistatus.tpl', params,
                              context_instance=RequestContext(request))
