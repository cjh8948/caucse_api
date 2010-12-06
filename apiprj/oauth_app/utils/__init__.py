import uuid, hashlib

def _mysql_password(password):
    """Python implementation of MySQL PASSWORD() function."""
    phase1 = hashlib.sha1(password).digest()
    phase2 = hashlib.sha1(phase1).hexdigest()
    return "*" + phase2.upper()

def _mysql_oldpassword(password):
    """Python implementation of MySQL OLD_PASSWORD() function."""
    nr, add, nr2, mask = 1345345333L, 7L, 0x12345671L, 0x7FFFFFFFL;
    for c in password:
        if c in ' \t': continue
        c = ord(c)
        nr ^= (((nr & 63) + add) * c) + (nr << 8)
        nr2 += (nr2<<8) ^ nr
        add += c
    return "%016x"% (((nr & mask) << 32) | (nr2 & mask))

def check_mysql_password(raw, hashed):
    if len(hashed) == 16:
        return _mysql_oldpassword(raw) == hashed
    return _mysql_password(raw) == hashed
