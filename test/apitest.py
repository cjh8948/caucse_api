from secure import URL_PREFIX 
import unittest, json, urllib, urllib2

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
        keys = [u'name', u'mobile', u'id', u'img_url', u'email', 
                u'entrance_year']
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
