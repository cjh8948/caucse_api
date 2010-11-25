from django.core.exceptions import ObjectDoesNotExist
import oauth2 as oauth
import models
import uuid
import hashlib

def oauth_required(func):
    def verify_request(request, *arg, **keywords):
        server = AuthServer()
        params = server.verify_access_django_request(request)
        return func(request, *arg, **keywords)
    return verify_request

def oauth_verify(func):
    def verify_request(request, *arg, **keywords):
        server = AuthServer()
        params = server.verify_django_request(request)
        return func(request, *arg, **keywords)
    return verify_request

def mysql_password(password):
    phase1 = hashlib.sha1(password).digest()
    phase2 = hashlib.sha1(phase1).hexdigest()
    return "*"+phase2.upper()

def generate_token():
    return str(uuid.uuid4()).replace('-','')

def new_request_token(consumer_key, callback=None):
    token = models.Token(key=generate_token(), secret=generate_token(),
                         consumer=models.Consumer.objects.get(key=consumer_key),
                         type="R", callback=callback)
    token.save()

    oauth_token = oauth.Token(token.key, token.secret)
    oauth_token.set_callback(token.callback)
    return oauth_token
    

class AuthServer(oauth.Server):
    def __init__(self, signature_methods=None):
        """currently AuthServer supports only SHA1 signature."""
        sha1_signature_method = {'HMAC-SHA1':oauth.SignatureMethod_HMAC_SHA1()}
        self.signature_methods = signature_methods or sha1_signature_method

    def conv_oauthrequest(self, django_request):
        """ This method converts django.http.HttpRequest into oauth.Request.
        """
        # build auth_header
        auth_header = {}
        if 'Authorization' in django_request.META:
            auth_header = {'Authorization': 
                           django_request.META['Authorization']}
        elif 'HTTP_AUTHORIZATION' in django_request.META:
            auth_header =  {'Authorization': 
                            django_request.META['HTTP_AUTHORIZATION']}

        # build parameters, query string
        parameters = dict(django_request.REQUEST)
        qs = django_request.META['QUERY_STRING']

        # make oauth.Request object
        request = oauth.Request\
                       .from_request(django_request.method,
                                     django_request.build_absolute_uri(),
                                     headers=auth_header,
                                     parameters=parameters,
                                     query_string=qs)

        return request

    def verify_django_request(self, django_request):
        request = self.conv_oauthrequest(django_request)
        consumer = self.fetch_consumer(request['oauth_consumer_key'])
        token = None
        if 'oauth_token' in request:
            token = self.fetch_token(request['oauth_token'])
        return self.verify_request(request, consumer, token)

    def verify_access_django_request(self, django_request):
        request = self.conv_oauthrequest(django_request)
        consumer = self.fetch_consumer(request['oauth_consumer_key'])
        token = models.Token.objects.get(key=request['oauth_token'])
        if token.type != "A":
            raise Exception("no access token")
        return self.verify_request(request, consumer, token)

    def fetch_consumer(self, consumer_key):
        consumer = models.Consumer.objects.get(key=consumer_key)
        return oauth.Consumer(consumer.key, consumer.secret)

    def fetch_token(self, token_key):
        token = models.Token.objects.get(key=token_key)
        return oauth.Token(key=token.key, secret=token.secret)

    def new_token(self, token_type):
        pass
