from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/artists')
def artists():
    return render_template('artists.html')


@app.route('/new_artists')
def new_artists():
    return render_template('new_artists.html')

@app.route('/artist')
def artist():
    return render_template('artist.html')
