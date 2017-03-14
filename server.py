"""Welcome to the Neighborhood"""

# -*- coding: utf-8 -*-

from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session, g
from flask_debugtoolbar import DebugToolbarExtension
# from os import environ



app = Flask(__name__)

app.secret_key = 'secret'
# api_key = environ['GOOGLE_API_KEY']

app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """Homepage"""

    return render_template('index.html')




if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
