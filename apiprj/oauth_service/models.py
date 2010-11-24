from django.db import models
import oauth2 as oauth
import random

class Consumer(models.Model):
    TYPE_CHOICES = (('C', 'CLIENT'),('B','BROWSER'))

    key = models.CharField(unique=True, max_length=255)
    secret = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=20)
    description = models.TextField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, 
                            default='C')
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.key

class Token(models.Model):
    TYPE_CHOICES = (('R', 'REQUEST'), ('A','ACCESS'))

    key = models.CharField(unique=True, max_length=255, primary_key=True)
    secret = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    consumer = models.ForeignKey('Consumer')
    callback = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(blank=True, max_length=20)
    verifier = models.CharField(blank=True, max_length=255)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def generate_token(self):
        return str(uuid.uuid4()).replace('-','')

    def new_verifier(self):
        if self.type == 'A':
            raise Exception

        self.verifier = "%06d"%random.randint(0,999999)
        self.save()

    def promote_to_access(self):
        if self.type == 'A':
            raise Exception
        self.key = self.generate_token()
        self.secret = self.generate_token()
        self.type = 'A'
        self.save()

    def to_oauth_token(self):
        token = oauth.Token(self.key, self.secret)
        if self.callback:
            token.set_callback(self.callback)
        if self.verifier:
            token.set_verifier(self.verifier)
        return token
