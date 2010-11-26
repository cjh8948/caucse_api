from apiprj.oauth_app import models
import oauth2 as oauth
import uuid, hashlib

def mysql_password(password):
    phase1 = hashlib.sha1(password).digest()
    phase2 = hashlib.sha1(phase1).hexdigest()
    return "*" + phase2.upper()

def new_request_token(consumer_key, callback=None):
    def generate_token():
        return str(uuid.uuid4()).replace('-', '')
    
    consumer = models.Consumer.objects.get(key=consumer_key)
    token = models.Token(key=generate_token(), secret=generate_token(),
                         consumer=consumer, type="R", callback=callback)
    token.save()

    return token.to_oauth()
