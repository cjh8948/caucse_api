from django.db import models
import oauth2 as oauth

class Consumer(models.Model):
    TYPE_CHOICES = (('Client', 'Client'),('Browser','Browser'))

    key = models.CharField(unique=True, max_length=255, primary_key=True)
    secret = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=20)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, 
                            default='Client')
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.key

class Token(models.Model):
    TYPE_CHOICES = (('REQUEST', 'request'), ('ACCESS','access'))

    key = models.CharField(unique=True, max_length=255, primary_key=True)
    secret = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    consumer = models.ForeignKey('Consumer')
    callback = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(blank=True, max_length=20)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Nonce(models.Model):
    key = models.CharField(max_length=255, primary_key=True)
    token_key = models.CharField(max_length=255)
    consumer_key = models.CharField(max_length=255)
    
