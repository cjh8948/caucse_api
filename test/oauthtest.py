from secure import OAUTH_URL_PREFIX 
import unittest, urlparse
import oauth2 as oauth

CONSUMER_KEY = 'consumer_key'
CONSUMER_SECRET = 'consumer_secret'
REQUEST_TOKEN_URL = OAUTH_URL_PREFIX+'request_token'
ACCESS_TOKEN_URL = OAUTH_URL_PREFIX+'access_token'
AUTHORIZE_URL = OAUTH_URL_PREFIX+'authorize'

class OauthTestCase(unittest.TestCase): 
    def test_request_token(self):
        consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        client = oauth.Client(consumer)
        resp, content = client.request(REQUEST_TOKEN_URL, "GET")
        self.assertEquals(resp['status'], '200')

        request_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(resp.has_key('oauth_token'))
        self.assertTrue(resp.has_key('oauth_token_secret'))

if __name__ == '__main__':
    unittest.main()
