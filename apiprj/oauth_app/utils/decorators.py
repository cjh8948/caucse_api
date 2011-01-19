#!-*-coding:utf8-*-
"""oauth 인증이 필요한 view function에 대한 데코레이터"""
from django.http import HttpResponseBadRequest
from oauthserver import ServerAlpha
from functools import wraps

def oauth_required(view_func):
    """oauth 인증이 필요한 django view function에 대한 데코레이터 함수.
    해당 view는 반드시 oauth_params을 인자로 받는다.
    """
    
    def verify_request(request, *arg, **keywords):
        keywords['oauth_params'] = ServerAlpha().verify_access_request(request)
        return view_func(request, *arg, **keywords)
    
    return wraps(view_func)(verify_request)

def oauth_verify(view_func):
    """\
    oauth flow request가 유효한지 검증이 필요한 django view function에 대한 
    데코레이터 함수. 해당 view는 반드시 oauth_params을 인자로 받는다.

    요청이 유효하지 않은 경우 HttpResponseBadRequest(400 status code)을 반환
    """
    
    def verify_request(request, *arg, **keywords):
        try:
            keywords['oauth_params'] = ServerAlpha().verify_flow_request(request)
        except:
            return HttpResponseBadRequest()
        return view_func(request, *arg, **keywords)
    
    return wraps(view_func)(verify_request)
