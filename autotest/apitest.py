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
            url += '?' + urllib.urlencode(param).replace('+', '%20')
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
        listinfo = obj['listinfo']
        self.assertEqual(listinfo['board_id'], 'board_alumni99')
        self.assertEqual(listinfo['per_page'], len(obj['articles']))

    def test_list_restful(self):
        'GET articles/list/board_alumni99 with oauth'
        resp, content = self.oauth_get('articles/list/board_alumni99',
                                       self.consumer, self.access_token)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        listinfo = obj['listinfo']
        self.assertEqual(listinfo['board_id'], 'board_alumni99')
        self.assertEqual(listinfo['per_page'], len(obj['articles']))
    
    def test_list_restful_with_q(self):
        'GET articles/list/board_alumni99;q=gochi'
        param = {'q':u'gochi'}
        resp, content = self.oauth_get("articles/list/board_alumni99",
                                       self.consumer, self.access_token,
                                       param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        listinfo = obj['listinfo']
        articles = obj['articles']
        self.assertEqual(listinfo['board_title'], u'99학번 게시판')
        self.assertEqual(listinfo['page'], 0)
        for article in articles:
            check = ((u'gochi' in article['author']['id']) or 
                     (u'gochi' in article['content']) or
                     (u'gochi' in article['title']) or
                     (u'gochi' in article['author']['name']))
            self.assertTrue(check)
    
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
                 'message': u'message 한글 메시지 테스트.'.encode('utf8')}
        resp, content = self.oauth_post("articles/create", self.consumer,
                                        self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        status = obj['status']
        article = obj['article']
        self.assertEqual(status, 'ok')
        self.assertEqual(article['title'], param['title'])
        self.assertEqual(article['content'].encode('utf8'), param['message'])

    def test_create_restful(self):
        'POST articles/create/board_alumni99 with oauth'        
        param = {'title': 'title restful', 'message': 'message restful'}
        resp, content = self.oauth_post("articles/create/board_alumni99",
                                        self.consumer, self.access_token,
                                        param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'ok')
    
    def test_update(self):
        'POST articles/update/board_alumni99/:article_id'
        # create first
        param = {'title': 'title!', 'message': 'message!'}
        resp, content = self.oauth_post('articles/create/board_alumni99',
                                        self.consumer, self.access_token,
                                        param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        status = obj['status']
        self.assertEqual(status, 'ok')
        article_id = obj['article']['id']
        
        # and then update
        new_message = 'message changed!!!!!'
        param = {'title': 'title!!!', 'message': new_message}
        url = 'articles/update/board_alumni99/%d' % article_id
        resp, content = self.oauth_post(url, self.consumer, self.access_token,
                                        param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        status = obj['status']
        self.assertEqual(status, 'ok')
        article = obj['article']
        self.assertEqual(article['content'], new_message)

    def test_create_on_photo_restful(self):
        'POST articles/create/photo_alumni99 with oauth'        
        param = {'title': 'title restful', 'message': 'message restful'}
        resp, content = self.oauth_post("articles/create/photo_alumni99",
                                        self.consumer, self.access_token,
                                        param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        self.assertEqual(obj['status'].lower(), 'error')
        self.assertTrue(u'지원하지 않습니다.' in obj['message'])
        
    def test_delete(self):
        'GET articles/delete/board_alumni99/:id'
        # create something to delete
        param = {'title': 'title? ...?', 'message': 'message is...'}
        resp, content = self.oauth_post('articles/create/board_alumni99',
                                        self.consumer, self.access_token,
                                        param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        article_id = obj['article']['id']
        
        # delete it
        delete_url = 'articles/delete/board_alumni99/%d' % article_id
        resp, content = self.oauth_get(delete_url, self.consumer,
                                       self.access_token)
        obj = json.loads(content)
        self.assertEqual(resp['status'], '200')
        
        
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
        status = obj['status']
        comment = obj['comment']
        self.assertEqual(obj['status'].lower(), 'ok')
        self.assertEqual(comment['content'], param['message'])

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
    
    def test_delete(self):
        'GET comments/delete/board_alumni99/:comment_id'
        # create first
        param = {'board_id':'board_alumni99', 'article_id':'20',
                 'message':'comment test'}
        resp, content = self.oauth_post("comments/create", self.consumer,
                                        self.access_token, param)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        status = obj['status']
        comment = obj['comment']
        self.assertEqual(status, 'ok')
        self.assertEqual(comment['content'], param['message'])
        comment_id = comment['id']
        
        # and then delete
        comment_url = 'comments/delete/board_alumni99/%d' % comment_id
        resp, content = self.oauth_get(comment_url, self.consumer,
                                      self.access_token)
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        status = obj['status']
        self.assertEqual(status, 'ok')

class FavoriteTest(ApiTestCase):
    def test_list(self):
        "GET favorties/list with oauth"
        resp, content = self.oauth_get('favorites/list', self.consumer,
                                       self.access_token)        
        self.assertEqual(resp['status'], '200')
        obj = json.loads(content)
        ids = [board['board_id'] for board in obj]
        self.assertTrue('board_alumni99' in ids)


class OauthTestCase(ApiTestCase):
    def test_request_token(self):
        'GET oauth/request_token'
        resource = "oauth/request_token"
        resp, content = self.oauth_get(resource=resource,
                                       consumer=self.consumer,
                                       token=None, param=None,
                                       callback="oob")
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
    
    def test_show_no_user_id(self):
        'GET users/show with oauth'
        resp, content = self.oauth_get('users/show', self.consumer,
                                       self.access_token)
        self.assertEqual(resp['status'], '200')
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
        id_list = map(lambda x: x['id'], obj)
        self.assertTrue('reset' in id_list)
        
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
        self.assertTrue(set(('gochi', 'jeppy', 'reset')).issubset(id_list))


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
