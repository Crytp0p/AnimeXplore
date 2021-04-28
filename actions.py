import requests
from urllib.parse import quote
import json

import Keys


def search(anime):
    url = "https://simpleanime.p.rapidapi.com/anime/search/"

    headers = {
        'x-rapidapi-key': Keys.API_KEY,
        'x-rapidapi-host': "simpleanime.p.rapidapi.com"
    }

    # parse the name of the anime as a get-response quey
    parsed_query = quote(anime)

    url = url + parsed_query

    # response is a str
    response = requests.request("GET", url, headers=headers)

    # convert string to json => dictionary, acess data  which is a list
    res_data = json.loads(response.text)['data']

    # Each list member is a dictionary itself with fields cover,title,date and vid_id(video ID)
    return res_data


def download(video_id):
    url = "https://simpleanime.p.rapidapi.com/anime/info/videos/"

    headers = {
        'x-rapidapi-key': Keys.API_KEY,
        'x-rapidapi-host': "simpleanime.p.rapidapi.com"
        }

    url = url + video_id

    response = requests.request("GET", url, headers=headers)

    res = json.loads(response.text)

    return res
