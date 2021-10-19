from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import NewArtistForm
from app.models import Artist, Event, ArtistToEvent, Venue


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/artists')
def artists():
    artist_list = {'John Browns Body',
                   'The Gun Poets',
                   'Donna The Buffalo',
                   'The Blind Spots'}
    return render_template('artists.html', artist_list=artist_list)


@app.route('/artist')
def artist():
    info = [
        {
            'artist': 'The Gun Poets',
            'hometown': 'Beautiful day in Portland!',
            'description': 'Voice as a weapon, words as bullets, spreading the universal message of peace, love, '
                           'and justice through music. Sure, theres a cynical cultural tendency to make certain '
                           'assumptions when you hear the word "gun" associated with rap music, but this seven-member '
                           'live hip-hop band from Ithaca, NY, runs contrary to that image with their positive '
                           'message and uplifting performances. ',
            'events': {'The Commons on Thursday 9/6',
                       'The Haunt next Friday 9/14'}
        }
    ]
    return render_template('artist.html', info=info)


@app.route('/new_artists', methods=['GET', 'POST'])
def new_artists():
    form = NewArtistForm()
    if form.validate_on_submit():
        flash('New artist created: {}'.format(
            form.artist.data))
        return redirect(url_for('new_artists'))
    return render_template('new_artists.html', title='Create a New Artist', form=form)


@app.route('/populate_db')
def populate_db():
    clear_db()

    a1 = Artist(artistname='The Gun Poets',
                hometown='Ithaca',
                description='Ithaca Hip Hop Band')
    a2 = Artist(artistname='Stone Cold Miracle',
                hometown='Fall Creek',
                description='Funky Soul')
    a3 = Artist(artistname='The New Team',
                hometown='San Francisco',
                description='They play new-age music. It sux.')
    db.session.add_all([a1, a2, a3])
    db.session.commit()

    e1 = Event(eventname="Coachella", date='10/30/21')
    e2 = Event(eventname="Lalapalooza", date='11/7/21')
    e3 = Event(eventname="Octoberfest", date='10/6/22')
    e4 = Event(eventname="Governors Ball", date='12/15/21')
    e5 = Event(eventname="Woodstock", date='12/26/21')
    db.session.add_all([e1, e2, e3, e4, e5])
    db.session.commit()

    v1 = Venue(eventname="Madison Square Garden", date='10/30')
    v2 = Venue(eventname="The Greek Theatre", date='11/7')
    v3 = Venue(eventname="The Dock", date='11/6')
    db.session.add_all([v1, v2, v3])
    db.session.commit()
    flash("Database has been populated")
    return render_template('base.html', title='Home')


def clear_db():
    flash("Resetting database: deleting old data and repopulating with dummy data")
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()
