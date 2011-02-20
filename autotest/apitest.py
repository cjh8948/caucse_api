#-*-coding:utf8-*-
from secure import (ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY,
                    CONSUMER_SECRET, URL_PREFIX)
from oauthclient import ClientAlpha
import unittest, json, urllib, urlparse, oauth2
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


    def oauth_delete(self, resource, consumer, token):
        url = URL_PREFIX + resource
        client = ClientAlpha(consumer, token)
        resp, content = client.request(url, "DELETE")
        return resp, content

    def oauth_get(self, resource, consumer, token, param=None, callback=None):
        url = self._get_url(resource, param)
        client = ClientAlpha(consumer, token)
        if callback: client.set_callback(callback)
        resp, content = client.request(url, "GET")
#        print resource
#        try:
#            s = json.dumps(json.loads(content),indent=4,ensure_ascii=False)
#            print s.encode('utf8')
#        except:
#            pass
        return resp, content

    def oauth_post(self, resource, consumer, token, param={}, callback=None):
        url = URL_PREFIX + resource
        client = ClientAlpha(consumer, token)
        if callback: client.set_callback(callback)
        body = urllib.urlencode(param)
        resp, content = client.request(url, "POST", body=body)
#        print resource
#        try:
#            s =  json.dumps(json.loads(content),indent=4,ensure_ascii=False)
#            print s.encode('utf8')
#        except Exception as e:
#            print e
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
        self.assertEqual(obj['entrance_year'], 1999)

        # validate keys
        keys = [u'name', u'mobile', u'img_url', u'introduce', u'id',
                u'birthday', u'messenger', u'homepage', u'email', u'entrance_year']
        self.assertEqual(obj.keys(), keys)



class CafeTest(ApiTestCase):
    def test_cafe_list(self):
        'GET cafe/list'
        resp, content = self.oauth_get('cafe/list', self.consumer, self.access_token)

        self.assertEqual(resp['status'], '200')

        obj = json.loads(content)

        listinfo = obj['listinfo']
        self.assertEqual(listinfo['q'], u'')
        self.assertEqual(listinfo['total_cafes'], 5)
        self.assertEqual(listinfo['total_matched_cafes'], 5)

        f = open("test.txt", 'w')
        f.write(content)
        f.close()
        
        cafes = obj['cafes']

        self.assertEqual(cafes[0]['admin'], 'hyojeong28')
        self.assertEqual(cafes[1]['member_list'][0], 'jeppy')


    def test_cafe_list_q(self):
        'GET cafe/list?q=기획""'
        param = {'q':u'기획'.encode('utf-8')}
        resp, content = self.oauth_get('cafe/list', self.consumer, self.access_token, param)

        self.assertEqual(resp['status'], '200')

        obj = json.loads(content)

        listinfo = obj['listinfo']
        self.assertEqual(listinfo['q'], u'기획')
        self.assertEqual(listinfo['total_cafes'], 5)
        self.assertEqual(listinfo['total_matched_cafes'], 1)

        cafes = obj['cafes']

        for cafe in cafes:
            check = ((u'gochi' in cafe['member_list']) or
                     (u'기획총무부' in cafe['cafe_name']) or
                     (u'hyojeong28' in cafe['admin']))
            self.assertTrue(check)

if __name__ == '__main__':
    unittest.main()
