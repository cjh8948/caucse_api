from django.core.exceptions import ObjectDoesNotExist
import oauth2 as oauth
import models

def initialize_server_request(request):
    auth_header = {}
    if request.META.has_key('Authorization'):
        auth_header['Authorization'] = request.META['Authorization']
    elif request.META.has_key('HTTP_AUTHORIZATION'):
        auth_header['Authorization'] = request.META['HTTP_AUTHORIZATION']

    parameters = {}
    if request.method == "POST" and\
       request.META['CONTENT_TYPE'] == 'applicaion/x-www-form-urlencoded':
        parameters = dict(request.REQUEST.items())

    query_string = request.META.get('QUREY_STRING','')
    oauth_request = oauth.Request.from_request(request.method,
                                               request.build_absolute_uri(),
                                               headers=auth_header,
                                               parameters=parameters,
                                               query_string=query_string)

    if oauth_request:
        server = oauth.Server()
        server.add_signature_method(oauth.SignatureMethod_HMAC_SHA1())
    else:
        server = None

    return server, oauth_request

class OAuthModelWrapper:
    def lookup_consumer(self, key):
        try:        
            c = models.Consumer.objects.get(key=key)
            return oauth.Consumer(c.key, c.secret)
        except ObjectDoesNotExist:
            return None

    def lookup_token(self, token_type, token):
        try:
            t = models.Token.object.get(key=token)
            return oauth.Token(t.key, t.secret)
        except ObjectDoesNotExist:
            return None

    def lookup_nonce(self, consumer, token, nonce):
        try:
            n = models.Nonce.objects.get(key=nonce)
            return n.key
        except ObjectDoesNotExist:
            return None

    def fetch_request_token(self, consumer, callback):
        pass
            
         


