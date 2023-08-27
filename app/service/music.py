from app.utils.db import DBUtils

class MusicService:
    def __init__(self):
        self.db_utils = DBUtils()
        self.music = "Music Service Class"

    def get_music_page(self):
        sql = """
        SELECT * FROM user WHERE id = 'test';
        """
        row = self.db_utils.query(sql, ())
        return row
