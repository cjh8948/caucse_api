from apiprj.ext import oauth2
from apiprj.exceptions import AuthError
from django.db import models
import random, uuid, datetime

class Consumer(models.Model):
    key = models.CharField(unique=True, max_length=255)
    secret = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=20)
    description = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def to_oauth(self):
        return oauth2.Consumer(self.key, self.secret)

    def __unicode__(self):
        return self.key

class Token(models.Model):
    TYPE_CHOICES = (('R', 'REQUEST'), ('A', 'ACCESS'))

    key = models.CharField(unique=True, max_length=255)
    secret = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    consumer = models.ForeignKey('Consumer')
    callback = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(blank=True, max_length=20)
    verifier = models.CharField(blank=True, max_length=255)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_token():
        return str(uuid.uuid4()).replace('-', '')

    @classmethod
    def new_request_token(cls, consumer_key, callback=None):
        consumer = Consumer.objects.get(key=consumer_key)
        token = cls(key=cls.generate_token(), secret=cls.generate_token(),
                    consumer=consumer, type="R", callback=callback)
        token.save()
        
        # delete old request token (3min)
        three_min_ago = datetime.datetime.now() - datetime.timedelta(minutes=3)
        try: 
            cls.objects.filter(type="R")\
                       .filter(modified__lte=three_min_ago)\
                       .delete()
        except Exception as e:
            print e
        
        return token
    
    def new_verifier(self, user):
        if self.type == 'A':
            raise AuthError
        self.user = user
        self.verifier = "%06d" % random.randint(0, 999999)
        self.save()

    def promote_to_access(self):
        # delete user's old access token
        try:
            objs = Token.objects.filter(consumer=self.consumer)\
                                .filter(type='A')\
                                .filter(user=self.user)\
                                .exclude(key='access_token_key')
            objs.delete()
        except Exception as e:
            print e
                    
        # promote
        if self.type == 'A':
            raise AuthError('Access token cannot be promoted')
        self.key = self.generate_token()
        self.secret = self.generate_token()
        self.type = 'A'
        self.save()

    def to_oauth(self):
        token = oauth2.Token(self.key, self.secret)
        if self.callback:
            token.set_callback(self.callback)
        if self.verifier:
            token.set_verifier(self.verifier)
        return token
