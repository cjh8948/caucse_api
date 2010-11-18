from django.db import models

class Consumer(models.Model):
    TYPE_CHOICES = (('Client', 'Client'),('Browser','Browser'))

    key = models.CharField(unique=True, max_length=255)
    secret = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=20)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, 
                            default='Client')
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Token(models.Model):
    TYPE_CHOICES = (('REQUEST', 'request'), ('ACCESS','access'))

    key = models.CharField(unique=True, max_length=255)
    secret = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Nonce(models.Model):
    key = models.CharField(max_length=255)
    token_key = models.CharField(max_length=255)
    consumer_key = models.CharField(max_length=255)
    
