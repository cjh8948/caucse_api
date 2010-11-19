from django.core.exceptions import ObjectDoesNotExist
import oauth2 as oauth
import models

class AuthServer(oauth.Server):
    def __init__(self, signature_methods=None):
        sha1_signature_method = {'HMAC-SHA1':oauth.SignatureMethod_HMAC_SHA1()}
        self.signature_methods = signature_methods or sha1_signature_method

    def conv_oauthrequest(self, django_request):
        """ This method converts django.http.HttpRequest into oauth.Request.
        """
        parameters = dict(django_request.REQUEST)
        qs = django_request.META['QUERY_STRING']
        request = oauth.Request\
                       .from_request(django_request.method,
                                     django_request.build_absolute_uri(),
                                     parameters=parameters,
                                     query_string=qs)

        return request



