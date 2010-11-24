from secure import URL_PREFIX, TEST_USER, TEST_USER_PASSWORD
import unittest, json, urllib, urllib2, urlparse
from oauth_client_a import ClientAlpha
import oauth2 as oauth

CONSUMER_KEY = 'consumer_key'
CONSUMER_SECRET = 'consumer_secret'
REQUEST_TOKEN_KEY = 'request_token_key'
REQUEST_TOKEN_SECRET = 'request_token_secret'
ACCESS_TOKEN_KEY = 'access_token_key'
ACCESS_TOKEN_SECRET = 'access_token_secret'

class ApiTestCase(unittest.TestCase): 
    api = ""

    def get_url(self, param=None):
        url = URL_PREFIX + self.api
        if param: 
            url += '?' + urllib.urlencode(param)
        return url

    def oauth_get(self, consumer, token, param=None, callback=None):
        url = self.get_url(param)
        client = ClientAlpha(consumer, token)
        if callback: client.set_callback(callback)
        resp, content = client.request(url, "GET")
        return resp, content

    def oauth_post(self, consumer, token, param):
        url = URL_PREFIX + self.api
        client = ClientAlpha(consumer, token)
        body = urllib.urlencode(param)
        resp, content = client.request(url,"POST",body=body)
        return resp, content

    def plain_get(self, param):
        url = self.get_url(param)
        f = urllib2.urlopen(url)
        return f.read()

class RequestTokenTestCase(ApiTestCase):
    api = "oauth/request_token"

    def test_case_nocallback(self):
        consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        resp, content = self.oauth_get(consumer=consumer, token=None, 
                                       param=None)
        self.assertNotEquals(resp['status'], '200')

    def test_success_case(self):
        consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        resp, content = self.oauth_get(consumer=consumer, token=None, 
                                         param=None, 
                                         callback="http://callback.net")
        self.assertEquals(resp['status'], '200')
        request_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(request_token.has_key('oauth_token'))
        self.assertTrue(request_token.has_key('oauth_token_secret'))
        self.assertTrue(request_token.has_key('oauth_callback_confirmed'))

    def test_wrong_consumer_secret(self):
        consumer = oauth.Consumer(CONSUMER_KEY, "wrong_secret")
        client = ClientAlpha(consumer)
        resp, content = client.request(self.get_url(), "GET")
        self.assertNotEquals(resp['status'], '200')

class OauthAuthorizeTestCase(ApiTestCase):
    def setUp(self):
        # request token
        self.api = "oauth/request_token"
        self.consumer = consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        resp, content = self.oauth_get(consumer=consumer, token=None,
                                       param=None, callback="oob")
        self.assertEquals(resp['status'], '200')
        content_dict = dict(urlparse.parse_qsl(content))
        self.token = oauth.Token(content_dict['oauth_token'], 
                                 content_dict['oauth_token_secret'])

    def tearDown(self):
        self.api = "oauth/authorize"
        self.token = None

    def test_oauth_authorize(self):
        self.api = "oauth/authorize"
        params = {'user_id': TEST_USER, 'password':TEST_USER_PASSWORD}
        resp, content = self.oauth_post(self.consumer, self.token, params)
        self.assertEquals(resp['status'],'200')
        self.assertTrue('PIN:' in content)
        
    def test_oauth_authorize_with_wrong_password(self):
        self.api = "oauth/authorize"
        params = {'user_id': TEST_USER, 'password': "wrong_password"}
        resp, content = self.oauth_post(self.consumer, self.token, params)
        self.assertNotEquals(resp['status'],'200')
        


class AccessTokenTestCase(ApiTestCase):
    api = "oauth/access_token"

    def setUp(self):
        self.consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)

    def test_access_token(self):
        token = oauth.Token("request_token_key", "request_token_secret")
        token.set_verifier("1234")
        client = ClientAlpha(self.consumer, token)
        resp, content = client.request(self.get_url(), "POST")
        self.assertEquals(resp['status'],'200')
        access_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(access_token.has_key('oauth_token'))
        self.assertTrue(access_token.has_key('oauth_token_secret'))

    def test_wrong_token_secret(self):
        token = oauth.Token("request_token_key", "wrong_request_token_secret")
        token.set_verifier("1234")
        client = ClientAlpha(self.consumer, token)
        resp, content = client.request(self.get_url(), "POST")
        self.assertNotEquals(resp['status'],'200')
        access_token = dict(urlparse.parse_qsl(content))
        self.assertFalse(access_token.has_key('oauth_token'))
        self.assertFalse(access_token.has_key('oauth_token_secret'))

class UsersShowTest(ApiTestCase):
    api = "users/show"

    def test_gochi(self):
        # build oauth objects
        consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        token = oauth.Token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

        # make request
        param = {'user_id': 'gochi'}
        resp, content = self.oauth_get(consumer, token, param)
        self.assertEqual(resp['status'],'200')

        # validate result
        obj = json.loads(content)
        self.assertEqual(obj['id'], 'gochi')
        self.assertEqual(obj['name'], u'\uc774\ub355\uc900')
        self.assertEqual(obj['email'], 'gochist@gmail.com')
        self.assertEqual(obj['entrance_year'], 99)

        # validate keys
        keys = ['name', 'mobile', 'id', 'img_url', 'email', 'entrance_year']
        self.assertEqual(obj.keys(), keys)

class UsersLookupTest(ApiTestCase):
    api = "users/lookup"

    def test_wrong_access_token_secret(self):
        consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        token = oauth.Token(ACCESS_TOKEN_KEY, "worng_secret")
        param = {'user_id':'gochi,reset'}
        resp, content = self.oauth_get(consumer, token, param)
        self.assertNotEqual(resp['status'], 200)

    def test_gochi_reset(self):
        # build oauth objects
        consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        token = oauth.Token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

        # make request
        param = {'user_id':'gochi,reset'}
        resp, content = self.oauth_get(consumer, token, param)
        self.assertEqual(resp['status'],'200')

        # validate result
        obj = json.loads(content)
        self.assertEqual(len(obj),2)
        self.assertEqual(obj[0]['id'], 'gochi')
        self.assertEqual(obj[1]['id'], 'reset')

if __name__ == '__main__':
    unittest.main()
