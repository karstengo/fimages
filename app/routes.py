import time
from flask import render_template
from flask import send_from_directory
from helpers import get_pictures

from app import app


@app.route('/pictures/<path:path>')
def send_pictures(path):
    return send_from_directory(app.IMAGEBASEPATH, path)

@app.route('/test')
def atest():
    return render_template('test.html',
	title='Home', 
	)

@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def gallery(path):
    return render_template('gallery.html',
	title='Home', 
	path=path,
	pictures=get_pictures(path=path),
	)

