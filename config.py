import os

class Config(object):
    SECRET_KEY = os.environ.get('MY_SECRET_KEY_HERE') or 'you-will-never-guess'