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

@app.route('/gallery/<path:imgpath>', defaults={'imgpath':''})
def gallery(imgpath):

    logging.debug('22222222{} ... '.format(imgpath))
    pictures=get_pictures(path=imgpath)
    return render_template('gallery.html',
	path=imgpath,
        pictures=pictures,
	)

