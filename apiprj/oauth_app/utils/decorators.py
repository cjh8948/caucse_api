"""Functions in this module mark view functions and verify requests are vaild 
under oauth protocol."""
from oauthserver import ServerAlpha
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from functools import wraps

def oauth_required(view_func):
    """Marks view function to verify that the request is valid for 
    oauth required resources. 
    
    If the request is not valid, HttpResponseForbidden(403 status code) 
    will be returned.
    """
    def verify_request(request, *arg, **keywords):
        try:
            ServerAlpha().verify_access_request(request)
        except:
            return HttpResponseForbidden()
        return view_func(request, *arg, **keywords)
    
    return wraps(view_func)(verify_request)

def oauth_verify(view_func):
    """Marks view function to verify that a request is valid for oauth 
    authentication flow(1.0a).
    
    If the request is not valid, HttpResponseBadRequest(400 status code) 
    will be returned.
    """
    def verify_request(request, *arg, **keywords):
        try:
            ServerAlpha().verify_flow_request(request)
        except:
            return HttpResponseBadRequest()
        return view_func(request, *arg, **keywords)
    
    return wraps(view_func)(verify_request)
