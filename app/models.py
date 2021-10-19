from datetime import datetime
from app import db


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artistname = db.Column(db.String(64), index=True, unique=True)
    hometown = db.Column(db.String(64), index=True)
    description = db.Column(db.String(128), index=True)

    def __repr__(self):
        return '<Artist {}>'.format(self.artistname)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(64), index=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Event {}>'.format(self.eventname)


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venuename = db.Column(db.String(64), index=True)
    eventID = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Venue {}>'.format(self.venuename)


class ArtistToEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artistID = db.Column(db.Integer, index=True)
    eventID = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Event {}>'.format(self.eventname)
