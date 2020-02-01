from flask import Flask

app = Flask(__name__)
app.IMAGEBASEPATH='images/'

from app import routes

