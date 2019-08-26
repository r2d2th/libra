from app import app
from flask import render_template, redirect, url_for
from werkzeug.exceptions import NotFound, ServiceUnavailable
import requests


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', user='Docker')

