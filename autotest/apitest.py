from secure import *
from oauthclient import ClientAlpha
import unittest, re, json, urllib, urllib2, urlparse, oauth2

class ApiTestCase(unittest.TestCase): 
    
    def setUp(self):
        self.consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        self.access_token = oauth2.Token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET) 
    
    def get_url(self, resource, param=None):
        url = URL_PREFIX + resource
        if param: 
            url += '?' + urllib.urlencode(param)
        return url

    def oauth_get(self, resource, consumer, token, param=None, callback=None):
        url = self.get_url(resource, param)
        client = ClientAlpha(consumer, token)
        if callback: client.set_callback(callback)
        resp, content = client.request(url, "GET")
        return resp, content

    def oauth_post(self, resource, consumer, token, param={}):
        url = URL_PREFIX + resource
        client = ClientAlpha(consumer, token)
        body = urllib.urlencode(param)
        resp, content = client.request(url, "POST", body=body)
        return resp, content

    def plain_get(self, resource, param):
        url = self.get_url(resource, param)
        f = urllib2.urlopen(url)
        return f.read()
    
    def assertUserGochi(self, obj):
        self.assertEqual(obj['id'], 'gochi')
        self.assertEqual(obj['name'], u'\uc774\ub355\uc900')
        self.assertEqual(obj['email'], 'gochi@caucse.net')
        self.assertEqual(obj['entrance_year'], 99)

        # validate keys
        keys = ['name', 'mobile', 'id', 'img_url', 'email', 'entrance_year']
        self.assertEqual(obj.keys(), keys)

class RequestTokenTestCase(ApiTestCase):
    resource = "oauth/request_token"
    
    def test_case_nocallback(self):
        'oauth_get "oauth/request_token" without oauth_callback should return 400(Bad Request)'
        resp, content = self.oauth_get(self.resource, consumer=self.consumer,
                                       token=None, param=None)
        self.assertEquals(resp['status'], '400')
        self.assertEquals(content, "")

    def test_good_case(self):
        'oauth_get "oauth/request_token" should return oauth_token, oauth_secret, oauth_callback_confirmed'
        resp, content = self.oauth_get(resource=self.resource,
                                       consumer=self.consumer,
                                       token=None, param=None,
                                       callback="http://callback.net")
        self.assertEquals(resp['status'], '200')
        request_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(request_token.has_key('oauth_token'))
        self.assertTrue(request_token.has_key('oauth_token_secret'))
        self.assertTrue(request_token.has_key('oauth_callback_confirmed'))

    def test_wrong_consumer_secret(self):
        'oauth_get "oauth/request_token" with bad consumer secret should return 400(Bad Request)'
        consumer = oauth2.Consumer(CONSUMER_KEY, "wrong_secret")
        resp, content = self.oauth_get(resource=self.resource,
                                       consumer=consumer, token=None,
                                       param=None, callback="oob")
        # status code 400 is bad request
        self.assertEquals(resp['status'], '400') 
        self.assertEquals(content, "")

class OauthAuthorizeTestCase(ApiTestCase):
    def test_oauth_authorize(self):
        'Three legged oauth authentication 1.0a flow'
        # request token
        resp, content = self.oauth_get(resource="oauth/request_token",
                                       consumer=self.consumer, token=None,
                                       param=None, callback="oob")
        self.assertEquals(resp['status'], '200')
        content_dict = dict(urlparse.parse_qsl(content))
        token = oauth2.Token(content_dict['oauth_token'],
                             content_dict['oauth_token_secret'])

        # user authorize leg
        params = {'user_id': TEST_USER, 'password': TEST_USER_PASSWORD}
        resp, content = self.oauth_post(resource="oauth/authorize",
                                        consumer=self.consumer,
                                        token=token,
                                        param=params)
        self.assertEquals(resp['status'], '200')

        # parse verifier
        re_pin = re.compile("PIN: (\d*)")
        matched_obj = re_pin.search(content)
        self.assertNotEquals(matched_obj, None)
        verifier = matched_obj.groups()[0]

        # request access token
        token.set_verifier(verifier)
        resp, content = self.oauth_post(resource="oauth/access_token",
                                        consumer=self.consumer,
                                        token=token)
        self.assertEquals(resp['status'], '200')
        access_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(access_token.has_key('oauth_token'))
        self.assertTrue(access_token.has_key('oauth_token_secret'))

        # request protected resource
        param = {'user_id': 'gochi'}
        access_token = oauth2.Token(access_token['oauth_token'],
                                    access_token['oauth_token_secret'])
        resp, content = self.oauth_get(resource="users/show",
                                       consumer=self.consumer,
                                       token=access_token,
                                       param=param)
        self.assertEqual(resp['status'], '200')

        # validate result
        obj = json.loads(content)
        self.assertUserGochi(obj)
        
class UsersShowTest(ApiTestCase):
    def test_best_case(self):
        'oauth_get "users/show?user_id=gochi" should return user gochi in json format'
        # make request
        param = {'user_id': 'gochi'}
        resp, content = self.oauth_get(resource="users/show",
                                       consumer=self.consumer,
                                       token=self.access_token,
                                       param=param)
        self.assertEqual(resp['status'], '200')

        # validate result
        obj = json.loads(content)
        self.assertUserGochi(obj)
        
    def test_plain_get_case(self):
        'plain_get "users/show?user_id=gochi" should return 403(Forbidden)'

        plain_get_param = {'resource': "users/show",
                           'param': {'user_id': 'gochi'}}
        
        self.assertRaises(urllib2.HTTPError, self.plain_get, **plain_get_param)        

class UsersLookupTest(ApiTestCase):
    def test_best_case(self):
        'oauth_get "users/lookup?user_id=gochi,reset" should return users(gochi, reset) in json format'
        # make request
        param = {'user_id':'gochi,reset'}
        resp, content = self.oauth_get(resource="users/lookup",
                                       consumer=self.consumer,
                                       token=self.access_token,
                                       param=param)
        self.assertEqual(resp['status'], '200')

        # validate result
        obj = json.loads(content)
        self.assertEqual(len(obj), 2)
        self.assertUserGochi(obj[0])
        self.assertEqual(obj[1]['id'], 'reset')
    
    def test_plain_get_case(self):
        'plain_get "users/lookup?user_id=gochi,reset" should return 403(Forbidden)'

        plain_get_param = {'resource': "users/lookup",
                           'param': {'user_id': 'gochi,reset'}}
        
        self.assertRaises(urllib2.HTTPError, self.plain_get, **plain_get_param)

    def test_bad_token_secret(self):
        'oauth_get "users/lookup" with bad token secret should return 403(Forbidden)'
        # build oauth parameters
        token = oauth2.Token(ACCESS_TOKEN_KEY, "im_bad_secret")
        param = {'user_id': 'gochi,reset'}
        
        # make request
        resp, content = self.oauth_get(resource="users/lookup",
                                       consumer=self.consumer, token=token,
                                       param=param)
        
        # validate result - status code 403 is "Forbidden"
        self.assertEqual(resp['status'], '403')
        self.assertEqual(content, "")
        
class CommentsCreateTest(ApiTestCase):
    def test_comment_update(self):
        'oauth_post "comments/update" should return 200, and {"status":"ok"}'
        param = {'board_id':'board_alumni99', 'article_id':'20',
                 'message':'comment test'}
        resp, content = self.oauth_post("comments/create", self.consumer,
                                        self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'ok')

    def test_wrong_board(self):
        'oauth_post "comments/update" with board_id = board_not_registered, should return {"status":"error"}'
        param = {'board_id':'board_not_registered', 'article_id':'20',
                 'message':'comment test'}
        resp, content = self.oauth_post("comments/create", self.consumer,
                                        self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'error')
        
class ArticlesCreateTest(ApiTestCase):
    def test_articles_create(self):
        'oauth_post "articles/create" should return 200, and {"status":"ok"}'        
        param = {'board_id': 'board_alumni99', 'title': 'title',
                 'message': 'message'}
        resp, content = self.oauth_post("articles/create", self.consumer,
                                        self.access_token, param)
        print content
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'ok')
        
if __name__ == '__main__':
    unittest.main()
