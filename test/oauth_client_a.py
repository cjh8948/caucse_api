import httplib2
from urlparse import parse_qsl, urlparse
import oauth2 as oauth

class ClientAlpha(oauth.Client):
    """ClientAlpha is a worker to attempt to execute a request on flow 1.0a"""

    def __init__(self, consumer, token=None, cache=None, timeout=None, 
                 proxy_info=None, callback=None):

        oauth.Client.__init__(self, consumer, token, cache, timeout, proxy_info)
        self.callback = callback

    def set_callback(self, callback):
        self.callback = callback

    def request(self, uri, method="GET", body=None, headers=None, 
                redirections=httplib2.DEFAULT_MAX_REDIRECTS, 
                connection_type=None):
        """need to send callback"""

        DEFAULT_CONTENT_TYPE = 'application/x-www-form-urlencoded'

        if not isinstance(headers, dict):
            headers = {}
      
        is_multipart = method == 'POST' and \
                       headers.get('Content-Type', DEFAULT_CONTENT_TYPE) != \
                       DEFAULT_CONTENT_TYPE

        if body and method == 'POST' and not is_multipart:
            parameters = dict(parse_qsl(body))
            if self.callback: 
                parameters['oauth_callback'] = self.callback
        else:
            parameters = dict(parse_qsl(urlparse(uri).query))
            if self.callback: 
                parameters['oauth_callback'] = self.callback

        req = oauth.Request.from_consumer_and_token(self.consumer,
                                                    token=self.token,
                                                    http_method=method,
                                                    http_url=uri,
                                                    parameters=parameters)
        
        req.sign_request(self.method, self.consumer, self.token)

        if method == "POST":
            headers['Content-Type'] = headers.get('Content-Type', 
                                                 DEFAULT_CONTENT_TYPE)
            if is_multipart:
                headers.update(req.to_header())
            else:
                body = req.to_postdata()

        elif method == "GET":
            uri = req.to_url()
        else:
            headers.update(req.to_header())

        return httplib2.Http.request(self, uri, method=method, body=body,
                                     headers=headers, redirections=redirections,
                                     connection_type=connection_type)
