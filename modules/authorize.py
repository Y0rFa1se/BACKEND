from modules.redisdb import does_redis_exist, renew_redis_key

from dotenv import load_dotenv
import os

load_dotenv()

def req_to_host(request):
    return request.client.host

def is_local(request):
    host = req_to_host(request)

    if host.startswith("127.0.0.1") or host.startswith("localhost") or host.startswith("192.168.0.") or host.startswith("172.17.0.") or host.startswith("::1"):
        return True
    
    return False

def authorize(request, password):
    if is_local(request):
        return True
    
    host = req_to_host(request)
    
    if password == os.getenv("API_PASSWORD"):
        return True
    
    return False

def authorize_session(request, session_id=None):
    if session_id is None:
        return False
    
    if not does_redis_exist(session_id):
        return False
    
    renew_redis_key(session_id, 60*60)
    
    return True