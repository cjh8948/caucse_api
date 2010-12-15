#!-*-coding:utf8-*-
from secure import *
from oauthclient import ClientAlpha
import unittest, re, json, urllib, urlparse, oauth2
from httplib2 import Http

class ApiTestCase(unittest.TestCase): 
    def setUp(self):
        self.consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        self.access_token = oauth2.Token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET) 
    
    def _get_url(self, resource, param=None):
        url = URL_PREFIX + resource
        if param: 
            url += '?' + urllib.urlencode(param)
        return url

    def oauth_get(self, resource, consumer, token, param=None, callback=None):
        url = self._get_url(resource, param)
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
        url = self._get_url(resource, param)
        client = Http()
        resp, content = client.request(url, "GET")
        return resp, content
    
    def assertUserGochi(self, obj):
        self.assertEqual(obj['id'], 'gochi')
        self.assertEqual(obj['name'], u'\uc774\ub355\uc900')
        self.assertEqual(obj['email'], 'gochi@caucse.net')
        self.assertEqual(obj['entrance_year'], 99)

        # validate keys
        keys = [u'name', u'mobile', u'img_url', u'introduce', u'id',
                u'birthday', u'messenger', u'homepage', u'email', u'entrance_year']
        self.assertEqual(obj.keys(), keys)

class ArticlesTest(ApiTestCase):
    def test_list(self):
        'GET articles/list with oauth'
        param = {'board_id': 'board_alumni99'}
        resp, content = self.oauth_get('articles/list', self.consumer,
                                       self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        option = obj['option']
        self.assertEqual(option['board_id'], 'board_alumni99')
        self.assertEqual(option['per_page'], len(obj['articles']))

    def test_list_restful(self):
        'GET articles/list/board_alumni99 with oauth'
        resp, content = self.oauth_get('articles/list/board_alumni99',
                                       self.consumer, self.access_token)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        option = obj['option']
        self.assertEqual(option['board_id'], 'board_alumni99')
        self.assertEqual(option['per_page'], len(obj['articles']))
    
    def test_show(self):
        'GET articles/show with oauth'
        param = {'board_id': 'board_alumni99',
                 'article_id': '100'}
        resp, content = self.oauth_get('articles/show', self.consumer,
                                       self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['id'], 100)
        self.assertEqual(obj['author']['id'], 'gochi')

    def test_show_restful(self):
        'GET articles/show/board_alumni99/100 with oauth'
        resp, content = self.oauth_get('articles/show/board_alumni99/100',
                                       self.consumer, self.access_token)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['id'], 100)
        self.assertEqual(obj['author']['id'], 'gochi')

    def test_create(self):
        'POST articles/create with oauth'        
        param = {'board_id': 'board_alumni99', 'title': 'title',
                 'message': 'message'}
        resp, content = self.oauth_post("articles/create", self.consumer,
                                        self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'ok')

    def test_create_restful(self):
        'POST articles/create/board_alumni99 with oauth'        
        param = {'title': 'title restful', 'message': 'message restful'}
        resp, content = self.oauth_post("articles/create/board_alumni99",
                                        self.consumer, self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'ok')

    def test_create_on_photo_restful(self):
        'POST articles/create/photo_alumni99 with oauth'        
        param = {'title': 'title restful', 'message': 'message restful'}
        resp, content = self.oauth_post("articles/create/photo_alumni99",
                                        self.consumer, self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'error')
        self.assertTrue(u'지원하지 않습니다.' in obj['message'])
        
class BoardsTest(ApiTestCase):
    def test_lookup(self):
        'GET boards/lookup without oauth'
        param = {'board_id': 'board_alumni99,photo_alumni99'}
        resp, content = self.plain_get('boards/lookup', param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(len(obj), 2)
        
    def test_favorite(self):
        'GET boards/favorite with oauth'
        resp, content = self.oauth_get('boards/favorite', self.consumer,
                                       self.access_token)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertTrue(obj)
        
class CommentsTest(ApiTestCase):
    def test_create(self):
        'POST comments/create with oauth'
        param = {'board_id':'board_alumni99', 'article_id':'20',
                 'message':'comment test'}
        resp, content = self.oauth_post("comments/create", self.consumer,
                                        self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'ok')

    def test_create_restful(self):
        'POST comments/create/board_alumni99/20 with oauth'
        param = {'message':'restful comment test'}
        resp, content = self.oauth_post("comments/create/board_alumni99/20",
                                        self.consumer, self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'ok')

    def test_create_wrong_board(self):
        'POST comments/create on wrong board with oauth'
        param = {'board_id':'board_not_registered', 'article_id':'20',
                 'message':'comment test'}
        resp, content = self.oauth_post("comments/create", self.consumer,
                                        self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'error')

class FavoriteTest(ApiTestCase):
    def test_list(self):
        "GET favorties/list with oauth"
        resp, content = self.oauth_get('favorites/list', self.consumer,
                                       self.access_token)        
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj[0]['board_id'], 'board_part_plan')


class OauthTestCase(ApiTestCase):
    def test_request_token(self):
        'GET oauth/request_token'
        resource = "oauth/request_token"
        resp, content = self.oauth_get(resource=resource,
                                       consumer=self.consumer,
                                       token=None, param=None,
                                       callback="http://callback.net")
        self.assertEquals(resp['status'], '200')
        request_token = dict(urlparse.parse_qsl(content))
        self.assertTrue(request_token.has_key('oauth_token'))
        self.assertTrue(request_token.has_key('oauth_token_secret'))
        self.assertTrue(request_token.has_key('oauth_callback_confirmed'))

    def test_request_token_nocallback(self):
        'GET oauth/request_token without oauth_callback (expect 400)'
        resource = "oauth/request_token"
        resp, content = self.oauth_get(resource, consumer=self.consumer,
                                       token=None, param=None)
        self.assertEquals(resp['status'], '400')
        self.assertEquals(content, "")

    def test_request_token_wrong_consumer_secret(self):
        'GET oauth/request_token with bad consumer secret (expect 400)'
        resource = "oauth/request_token"
        consumer = oauth2.Consumer(CONSUMER_KEY, "wrong_secret")
        resp, content = self.oauth_get(resource=resource,
                                       consumer=consumer, token=None,
                                       param=None, callback="oob")
        # status code 400 is bad request
        self.assertEquals(resp['status'], '400') 
        self.assertEquals(content, "")

    def test_three_legged_oauth_authorize(self):
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

class UsersTest(ApiTestCase):
    def test_show(self):
        'GET users/show?user_id=gochi with oauth'
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
    
    def test_show_restful(self):
        'GET users/show/gochi with oauth'
        resp, content = self.oauth_get(resource='users/show/gochi',
                                       consumer=self.consumer,
                                       token=self.access_token)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertUserGochi(obj)
        
    def test_show_plain_get(self):
        'GET users/show?user_id=gochi without oauth'
        param = {'user_id': 'gochi'}
        resp, content = self.plain_get('users/show', param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'], 'error')

    def test_lookup(self):
        'GET users/lookup?user_id=gochi,reset with oauth'
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
    
    def test_lookup_plain_get(self):
        'GET users/lookup?user_id=gochi,reset without oauth'
        param = {'user_id': 'gochi,reset'}
        resp, content = self.plain_get('users/lookup', param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'], 'error')
        
    def test_lookup_bad_token_secret(self):
        'GET users/lookup with bad token secret'
        # build oauth parameters
        token = oauth2.Token(ACCESS_TOKEN_KEY, "im_bad_secret")
        param = {'user_id': 'gochi,reset'}
        
        # make request
        resp, content = self.oauth_get(resource="users/lookup",
                                       consumer=self.consumer, token=token,
                                       param=param)
        
        # validate result - "Invalid signature"
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'], "error")
        self.assertTrue("Invalid signature" in obj['message'])
    
    def test_search_name(self):
        u'GET users/search?q='
        param = {"q":u"e 천".encode('utf-8')}
        resp, content = self.oauth_get(resource="users/search",
                                       consumer=self.consumer,
                                       token=self.access_token,
                                       param=param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(len(obj), 1)
        self.assertEqual(obj[0]['id'], 'reset')
        
    def test_search_id(self):   
        'GET users/search?q=e'     
        param = {"q":u"e"}
        resp, content = self.oauth_get(resource="users/search",
                                       consumer=self.consumer,
                                       token=self.access_token,
                                       param=param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        id_list = map(lambda x: x['id'], obj)
        self.assertTrue(set(('jeppy', 'reset')).issubset(id_list))

    def test_search_enterance_year(self):   
        'GET users/search?q=99'     
        param = {"q":u"99"}
        resp, content = self.oauth_get(resource="users/search",
                                       consumer=self.consumer,
                                       token=self.access_token,
                                       param=param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        id_list = map(lambda x: x['id'], obj)
        self.assertTrue(set(('gochi', 'jeppy','reset')).issubset(id_list))


    def test_search_enterance_year_and_id(self):   
        'GET users/search?q=99+e'     
        param = {"q":u"99 e"}
        resp, content = self.oauth_get(resource="users/search",
                                       consumer=self.consumer,
                                       token=self.access_token,
                                       param=param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        id_list = map(lambda x: x['id'], obj)
        self.assertTrue(set(('jeppy', 'reset')).issubset(id_list))

    def test_search_two_names(self):   
        u'GET users/search?q=+'     
        param = {"q":u"석천 준".encode('utf-8')}
        resp, content = self.oauth_get(resource="users/search",
                                       consumer=self.consumer,
                                       token=self.access_token,
                                       param=param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        id_list = map(lambda x: x['id'], obj)
        self.assertTrue(set(('gochi', 'reset')).issubset(id_list))
        
if __name__ == '__main__':
    unittest.main()
