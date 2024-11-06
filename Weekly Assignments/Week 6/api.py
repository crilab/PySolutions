import requests
import json

url = 'https://football-frenzy.s3.eu-north-1.amazonaws.com/api'


def list_seasons():
    r = requests.get(url)
    r = json.loads(r.text)
    return r['seasons']


def list_gamedays(year):
    r = requests.get(f'{url}/{year}')
    r = json.loads(r.text)
    return r['gamedays']


def list_games(year, gameday):
    r = requests.get(f'{url}/{year}/{gameday}')
    r = json.loads(r.text)
    return r['games']
