import requests
from bs4 import BeautifulSoup

from app.service.music import MusicService
import dotenv
import os

dotenv.load_dotenv()

def get_raw():
    url = os.getenv("CRAWLING_URL")
    resp = requests.get(url)
    html = resp.content
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_result(soup):
    spotifydaily = soup.find(id="spotifydaily")
    raw_track_list = spotifydaily.find("tbody").find_all("tr")
    result = []
    for track in raw_track_list:
        infos = track.find("td","text mp").find("div").find_all("a")
        scores = track.find_all("td","np")
        artist = infos[0].string
        song = infos[1].string
        grade = int(scores[0].string)
        diff = scores[1].string
        result.append([grade, diff, song, artist])
        print(f"{grade} - {diff} - {song} - {artist}")
    return result

if __name__ == "__main__":
    soup = get_raw()
    result = get_result(soup)
    music_service = MusicService()
    music_service.insert_today_chart(result)
