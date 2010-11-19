from secure import OAUTH_URL_PREFIX 
import unittest, urlparse
import oauth2 as oauth

CONSUMER_KEY = 'consumer_key'
CONSUMER_SECRET = 'consumer_secret'
REQUEST_TOKEN_URL = OAUTH_URL_PREFIX+'request_token'
ACCESS_TOKEN_URL = OAUTH_URL_PREFIX+'access_token'
AUTHORIZE_URL = OAUTH_URL_PREFIX+'authorize'

class OauthTestCase(unittest.TestCase): 
    def setUp(self):
        self.consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        
    def test_request_token(self):
        client = oauth.Client(self.consumer)
        resp, content = client.request(REQUEST_TOKEN_URL, "GET")
        self.assertEquals(resp['status'], '200')
        request_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(request_token.has_key('oauth_token'))
        self.assertTrue(request_token.has_key('oauth_token_secret'))

    def test_access_token(self):
        token = oauth.Token("request_token_key", "request_token_secret")
        token.set_verifier("1234")
        client = oauth.Client(self.consumer, token)
        resp, content = client.request(ACCESS_TOKEN_URL, "POST")
        self.assertEquals(resp['status'],'200')

if __name__ == '__main__':
    unittest.main()
