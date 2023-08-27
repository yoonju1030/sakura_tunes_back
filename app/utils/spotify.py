import dotenv
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

class SpotifyUtils():
    def __init__(self):
        self.test = "test"
        self.client_credentials_manager = SpotifyClientCredentials(
            client_id=spotify_client_id, 
            client_secret=spotify_client_secret
        )
        self.sp = spotipy.Spotify(
            client_credentials_manager=self.client_credentials_manager
        )
        self.test="test"

    def get_artist(self, search_artist):
        try:
            result = self.sp.search(search_artist, type="artist")
            return result
        except Exception as e:
            raise e


        