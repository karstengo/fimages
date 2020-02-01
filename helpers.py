import os
import redis
from app import app

def get_pictures(path=None, pics=[]):
    if path != '.' and path != '/':
        files = [f for f in os.listdir(app.IMAGEBASEPATH + path) ]
        for f in files:
            pics.append(f)
    return pics

