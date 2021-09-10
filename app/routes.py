from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import NewArtistForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/artists')
def artists():
    return render_template('artists.html')


@app.route('/artist')
def artist():
    return render_template('artist.html')


@app.route('/new_artists', methods=['GET', 'POST'])
def new_artists():
    form = NewArtistForm()
    if form.validate_on_submit():
        flash('New artist created: {}'.format(
            form.artist.data))
        return redirect(url_for('new_artists'))
    return render_template('new_artists.html', title='Create a New Artist', form=form)
