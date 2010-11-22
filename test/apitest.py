from secure import URL_PREFIX, OAUTH_URL_PREFIX
import unittest, json, urllib, urllib2, urlparse
from oauth_client_a import ClientAlpha
import oauth2 as oauth

CONSUMER_KEY = 'consumer_key'
CONSUMER_SECRET = 'consumer_secret'
REQUEST_TOKEN_URL = OAUTH_URL_PREFIX+'request_token'
ACCESS_TOKEN_URL = OAUTH_URL_PREFIX+'access_token'
AUTHORIZE_URL = OAUTH_URL_PREFIX+'authorize'

class RequestTokenTestCase(unittest.TestCase):
    def test_success_case(self):
        consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        client = ClientAlpha(consumer)
        client.set_callback("http://callback.net")
        resp, content = client.request(REQUEST_TOKEN_URL, "GET")
        self.assertEquals(resp['status'], '200')
        request_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(request_token.has_key('oauth_token'))
        self.assertTrue(request_token.has_key('oauth_token_secret'))
        self.assertTrue(request_token.has_key('oauth_callback_confirmed'))

    def test_wrong_consumer_secret(self):
        consumer = oauth.Consumer(CONSUMER_KEY, "wrong_secret")
        client = ClientAlpha(consumer)
        resp, content = client.request(REQUEST_TOKEN_URL, "GET")
        self.assertNotEquals(resp['status'], '200')


class OauthTestCase(unittest.TestCase):
    def setUp(self):
        self.consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)

    def test_access_token(self):
        token = oauth.Token("request_token_key", "request_token_secret")
        token.set_verifier("1234")
        client = ClientAlpha(self.consumer, token)
        resp, content = client.request(ACCESS_TOKEN_URL, "POST")
        self.assertEquals(resp['status'],'200')
        access_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(access_token.has_key('oauth_token'))
        self.assertTrue(access_token.has_key('oauth_token_secret'))

    def test_wrong_token_secret(self):
        token = oauth.Token("request_token_key", "wrong_request_token_secret")
        token.set_verifier("1234")
        client = ClientAlpha(self.consumer, token)
        resp, content = client.request(ACCESS_TOKEN_URL, "POST")
        self.assertNotEquals(resp['status'],'200')
        access_token = dict(urlparse.parse_qsl(content))
        self.assertFalse(access_token.has_key('oauth_token'))
        self.assertFalse(access_token.has_key('oauth_token_secret'))

class ApiTestCase(unittest.TestCase): 
    api = ""

    def get_url(self, param=None):
        url = URL_PREFIX + self.api
        if param: 
            url += '?' + urllib.urlencode(param)
        return url

    def get_json_request(self, param=None):
        url = self.get_url(param)
        urlobj = urllib2.urlopen(url)
        obj = json.loads(urlobj.read())
        return obj

class UsersShowTest(ApiTestCase):
    api = "users/show"

    def test_gochi(self):
        # make request
        param = {'user_id': 'gochi'}
        obj = self.get_json_request(param)
        # validate result
        self.assertEqual(obj['id'], 'gochi')
        self.assertEqual(obj['name'], u'\uc774\ub355\uc900')
        self.assertEqual(obj['email'], 'gochist@gmail.com')
        self.assertEqual(obj['entrance_year'], 99)
        # validate keys
        keys = ['name', 'mobile', 'id', 'img_url', 'email', 'entrance_year']
        self.assertEqual(obj.keys(), keys)

class UsersLookupTest(ApiTestCase):
    api = "users/lookup"

    def test_gochi_reset(self):
        # make request
        param = {'user_id':'gochi,reset'}
        obj = self.get_json_request(param)
        # validate result
        self.assertEqual(len(obj),2)
        self.assertEqual(obj[0]['id'], 'gochi')
        self.assertEqual(obj[1]['id'], 'reset')

if __name__ == '__main__':
    unittest.main()
