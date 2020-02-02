import os
import redis
from app import app
import logging

def get_pictures(path=None):

    pics=[]

    logging.debug('yooo {} ... {}'.format(path, pics))
    if path != '.' and path != '/':
        fullpath = app.static_folder + '/images/' + path
        files = [f for f in os.listdir(fullpath) ]
        for f in files:
            pics.append(f)
    return pics

