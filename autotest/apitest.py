from secure import *
from oauthclient import ClientAlpha
import unittest, re, json, urllib, urllib2, urlparse, oauth2

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

    def oauth_post(self, consumer, token, param={}):
        url = URL_PREFIX + self.api
        client = ClientAlpha(consumer, token)
        body = urllib.urlencode(param)
        resp, content = client.request(url, "POST", body=body)
        return resp, content

    def plain_get(self, param):
        url = self.get_url(param)
        f = urllib2.urlopen(url)
        return f.read()

class RequestTokenTestCase(ApiTestCase):
    api = "oauth/request_token"

    def test_case_nocallback(self):
        consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        resp, content = self.oauth_get(consumer=consumer, token=None,
                                       param=None)
        self.assertNotEquals(resp['status'], '200')

    def test_success_case(self):
        consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        resp, content = self.oauth_get(consumer=consumer, token=None,
                                       param=None,
                                       callback="http://callback.net")
        self.assertEquals(resp['status'], '200')
        request_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(request_token.has_key('oauth_token'))
        self.assertTrue(request_token.has_key('oauth_token_secret'))
        self.assertTrue(request_token.has_key('oauth_callback_confirmed'))

    def test_wrong_consumer_secret(self):
        consumer = oauth2.Consumer(CONSUMER_KEY, "wrong_secret")
        client = ClientAlpha(consumer)
        resp, content = client.request(self.get_url(), "GET")
        self.assertEquals(resp['status'], '400') # Bad request error

class OauthAuthorizeTestCase(ApiTestCase):
    def test_oauth_authorize(self):
        # request token
        self.api = "oauth/request_token"
        consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        resp, content = self.oauth_get(consumer=consumer, token=None,
                                       param=None, callback="oob")
        self.assertEquals(resp['status'], '200')
        content_dict = dict(urlparse.parse_qsl(content))
        self.token = oauth2.Token(content_dict['oauth_token'],
                                  content_dict['oauth_token_secret'])

        # user authorize leg
        self.api = "oauth/authorize"
        params = {'user_id': TEST_USER, 'password': TEST_USER_PASSWORD}
        resp, content = self.oauth_post(consumer, self.token, params)
        self.assertEquals(resp['status'], '200')

        # parse verifier
        re_pin = re.compile("PIN: (\d*)")
        matched_obj = re_pin.search(content)
        self.assertNotEquals(matched_obj, None)
        verifier = matched_obj.groups()[0]

        # request access token
        self.api = "oauth/access_token"
        self.token.set_verifier(verifier)
        resp, content = self.oauth_post(consumer, self.token)
        self.assertEquals(resp['status'], '200')
        access_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(access_token.has_key('oauth_token'))
        self.assertTrue(access_token.has_key('oauth_token_secret'))

        # request restricted resource
        self.api = "users/show"
        param = {'user_id': 'gochi'}
        access_token = oauth2.Token(access_token['oauth_token'],
                                   access_token['oauth_token_secret'])
        resp, content = self.oauth_get(consumer, access_token, param)
        self.assertEqual(resp['status'], '200')

        # validate result
        obj = json.loads(content)
        self.assertEqual(obj['id'], 'gochi')
        self.assertEqual(obj['name'], u'\uc774\ub355\uc900')
        self.assertEqual(obj['email'], 'gochist@gmail.com')
        self.assertEqual(obj['entrance_year'], 99)

        # validate keys
        keys = ['name', 'mobile', 'id', 'img_url', 'email', 'entrance_year']
        self.assertEqual(obj.keys(), keys)

class UsersShowTest(ApiTestCase):
    api = "users/show"

    def test_gochi(self):
        # build oauth objects
        consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        token = oauth2.Token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

        # make request
        param = {'user_id': 'gochi'}
        resp, content = self.oauth_get(consumer, token, param)
        self.assertEqual(resp['status'], '200')

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
        consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        token = oauth2.Token(ACCESS_TOKEN_KEY, "worng_secret")
        param = {'user_id':'gochi,reset'}
        resp, content = self.oauth_get(consumer, token, param)
        self.assertNotEqual(resp['status'], 200)

    def test_gochi_reset(self):
        # build oauth objects
        consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        token = oauth2.Token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

        # make request
        param = {'user_id':'gochi,reset'}
        resp, content = self.oauth_get(consumer, token, param)
        self.assertEqual(resp['status'], '200')

        # validate result
        obj = json.loads(content)
        self.assertEqual(len(obj), 2)
        self.assertEqual(obj[0]['id'], 'gochi')
        self.assertEqual(obj[1]['id'], 'reset')

if __name__ == '__main__':
    unittest.main()
