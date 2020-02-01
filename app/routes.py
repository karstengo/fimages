import time
from flask import render_template
from flask import send_from_directory
from helpers import get_pictures

from app import app
import logging


@app.route('/pictures/<path:path>')
def send_pictures(path):
    return send_from_directory(app.IMAGEBASEPATH, path)

@app.route('/test')
def atest():
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

