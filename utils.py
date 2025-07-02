from cryptography.fernet import Fernet
from django.conf import settings

f = Fernet(settings.FERNET_SECRET_KEY)

def encrypt(data):
    return f.encrypt(data.encode()).decode()

def decrypt(data):
    return f.decrypt(data.encode()).decode()
