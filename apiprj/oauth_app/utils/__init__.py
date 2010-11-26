import uuid, hashlib

def mysql_password(password):
    """Python implementation of MySQL PASSWORD() function."""
    phase1 = hashlib.sha1(password).digest()
    phase2 = hashlib.sha1(phase1).hexdigest()
    return "*" + phase2.upper()