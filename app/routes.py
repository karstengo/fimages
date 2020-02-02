import time
from flask import render_template
from flask import send_from_directory
from helpers import get_pictures

from app import app
import logging


@app.route('/pictures/<path:imgpath>')
def send_pictures(imgpath):
    fullpath = 'images/' + imgpath
    logging.debug('Test {} ... '.format(fullpath))
    print(app.static_folder, fullpath)
    return send_from_directory(app.static_folder, fullpath)

@app.route('/test')
def atest():
    pictures=get_pictures(path='testimages')
    logging.debug('Test {} ... '.format(pictures))
    return render_template('test.html',
	title='Home', 
	)

@app.route('/gallery/<path:path>')
def gallery(path):

    logging.debug('22222222{} ... '.format(path))
    pictures=get_pictures(path=path)
    return render_template('gallery.html',
	path=path,
        pictures=pictures,
	)

