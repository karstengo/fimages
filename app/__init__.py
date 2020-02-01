from flask import Flask

app = Flask(__name__)
app.IMAGEBASEPATH='images/'
app.run(debug=True)

import logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

from app import routes
