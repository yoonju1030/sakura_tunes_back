from app.utils.db import DBUtils
from app.utils.spotify import SpotifyUtils

class MusicService:
    def __init__(self):
        self.db_utils = DBUtils()
        self.spotify_utils = SpotifyUtils()
        self.music = "Music Service Class"

    def get_music_page(self):
        try:
            sql = """
            SELECT * FROM user WHERE id = 'test';
            """
            row = self.db_utils.query(sql, ())
            return row
        except Exception as e:
            raise e

    def get_artist(self, artist):
        try:
            obj = self.spotify_utils.get_artist(artist)
            return obj
        except Exception as e:
            raise e