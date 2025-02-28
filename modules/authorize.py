from dotenv import load_dotenv
import os

load_dotenv()

def authorize(host, password):
    if host.startswith("127.0.0.1") or host.startswith("localhost") or host.startswith("192.168.0.") or host.startswith("172.17.0.") or host.startswith("::1"):
        return True
    
    if password == os.getenv("GUEST_PASSWORD"):
        return True
    
    return False