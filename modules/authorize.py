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