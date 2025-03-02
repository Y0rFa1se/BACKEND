import hashlib
import os

def get_hash(string):
    salt = string[-5:] + os.getenv("HASH_SALT")
    string = string + salt
    string = string.encode()

    string = hashlib.sha256(string).digest()
    string = hashlib.sha256(string)
    string = string.hexdigest()

    return string