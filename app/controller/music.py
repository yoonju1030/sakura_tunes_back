from flask import Blueprint, request
from app.service.music import MusicService

music = Blueprint("music", __name__,  url_prefix="/music")
music_service = MusicService()

@music.route("/", methods=["GET"])
def get_music_page():
    try:
        message = music_service.get_music_page()
        return message
    except Exception as e:
        return e

@music.route("/artist", methods=["POST"])
def get_chart():
    try:
        request_data = request.json
        message = music_service.get_artist(request_data["artist"])
        return message
    except Exception as e:
        return e