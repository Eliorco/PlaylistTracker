from datetime import datetime
from tracker_package import db


class Category(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(50), nullable=False)
    # tracks = db.relationship('PlaylistTracker', backref='tracks')

    def __repr__(self):
        return f"Category('{self.id}', '{self.name}', '{self.timestamp.strftime('%Y-%m-%d')}')"


class PlaylistTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_name = db.Column(db.String(50), nullable=False)
    track_id = db.Column(db.String(50), nullable=False)
    track_name = db.Column(db.String(50), nullable=False)
    playlist_index = db.Column(db.String(50), nullable=False)
    track_index = db.Column(db.String(50), nullable=False)
    artist_name = db.Column(db.String(50), nullable=False)
    popularity = db.Column(db.String(50), nullable=False)
    danceability = db.Column(db.String(50), nullable=False)
    loudness = db.Column(db.String(50), nullable=False)
    # user_id = db.Column(db.String(50), db.ForeignKey('category.name'), nullable=False)

    def to_dict(self):
        return {'trackId': self.track_id,
                'Timestamp': int(datetime.utcnow().timestamp()),
                'categoryName': self.category_name,
                'playlistName': self.playlist_name,
                'playlistIndex': self.playlist_index,
                'trackIndex': self.track_index,
                'trackName': self.track_name,
                'artistName': self.artist_name,
                'Popularity': int(self.popularity),
                'Danceability': float(self.danceability),
                'Loudness': float(self.loudness)
            }

    def __repr__(self):
        return f"PlaylistTracker('{self.track_name}', '{self.popularity}', '{self.playlist_name}', '{self.timestamp.strftime('%Y-%m-%d')}')"
