from oauthserver import ServerAlpha 

def oauth_required(func):
    def verify_request(request, *arg, **keywords):
        server = ServerAlpha()
        params = server.verify_access_django_request(request)
        return func(request, *arg, **keywords)
    return verify_request

def oauth_verify(func):
    def verify_request(request, *arg, **keywords):
        server = ServerAlpha()
        params = server.verify_django_request(request)
        return func(request, *arg, **keywords)
    return verify_request
