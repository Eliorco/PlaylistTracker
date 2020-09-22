# import asyncio
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .models import Category, PlaylistTracker
from tracker_package import db
import os

MAX_PLAYLISTS = 50


class Tracker:

    def __init__(self, category: str):
        category_exist = Category.query.filter_by(name=category).first()
        if not category_exist:
            try:
                db.session.add(Category(name=category))
                db.session.commit()
            except Exception as e:
                print(e)

        self.auth = SpotifyClientCredentials(client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
                                             client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'))
        self.category = category

    def search_category_playlists(self, sp) -> list:
        results_list = list()

        for i in [0, 50]:
            results = sp.search(q=f'top 100 {self.category}', type='playlist', offset=i, limit=MAX_PLAYLISTS)
            for _, playlist in enumerate(results['playlists']['items']):
                results_list.append(playlist['id'])

        return results_list

    def track(self, dry_run: bool = False) -> list:
        playlist_tracks_dict = {}
        tracks_to_add = list()
        sp = spotipy.Spotify(auth_manager=self.auth)
        category_playlist_list = self.search_category_playlists(sp)

        # iterate over 100 matching playlists
        for index, playlist_id in enumerate(category_playlist_list):
            playlist = sp.playlist(playlist_id)
            # iterate over 100 songs in playlist
            playlist_tracks_dict[playlist_id] = {
                'name': playlist['name'],
                'index': index,
                'tracks': {
                    track['track']['id']: {
                        'id': track['track']['id'],
                        'name': track['track']['name'],
                        'number': track['track']['track_number'],
                        'artist_name': track['track']['artists'][0]['name'],
                        'popularity': track['track']['popularity']
                    } for track in playlist['tracks']['items'] if track['track']['id']}
            }

        for current_playlist in playlist_tracks_dict.values():
            tracks = sp.audio_features(','.join(current_playlist['tracks']))
            for _, track in enumerate(tracks):

                current_track = current_playlist['tracks'][track['id']]
                try:
                    pt = PlaylistTracker(playlist_name=current_playlist.get('name'),
                                         playlist_index=current_playlist.get('index'),
                                         category_name=self.category,
                                         track_id=track.get('id'),
                                         track_name=current_track.get('name'),
                                         track_index=current_track.get('number'),
                                         artist_name=current_track.get('artist_name'),
                                         popularity=current_track.get('popularity'),
                                         danceability=track.get('danceability'),
                                         loudness=track.get('loudness'))
                    tracks_to_add.append(pt)
                except Exception as e:
                    print(e)

        if not dry_run:
            db.session.add_all(tracks_to_add)
            db.session.commit()

        return tracks_to_add
