from app import app
from flask import render_template, redirect, url_for
from werkzeug.exceptions import NotFound, ServiceUnavailable
import requests


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', user='Docker')


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


@app.route('/city')
def city():
    """
    Gets some data
    and then renders it.
    """
    try:
        req = requests.get("http://127.0.0.1:5001/cities")
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable("The Cities service is unavailable.")

    if req.status_code == 404:
        raise NotFound("No cities were found")

    data = req.json()
    cities = data['cities']
    return render_template('city.html', title='City Info', user='City Docker', cities=cities)


