import time
import json
import hashlib

import requests  # pip install requests to get this library
from .models import Character, Comic

PUBLIC_KEY = '9124cadeb528b8c0c8282cbaa39d6d22'
PRIVATE_KEY = '5b3761a41ecb79d455e70e6f27b1f8ff309ecf4c'

ts = str(time.time())
combined = ''.join([ts, PRIVATE_KEY, PUBLIC_KEY])
hash_value = hashlib.md5(combined.encode('ascii')).hexdigest()

# request_url = 'https://gateway.marvel.com/v1/public/characters/1009664/comics?ts=%s&apikey=%s&hash=%s' % (ts, PUBLIC_KEY, hash_value)

# r = requests.get(request_url)

def get_characters():
    global PUBLIC_KEY, hash_value, ts
    request_url = 'https://gateway.marvel.com/v1/public/characters?orderBy=-modified&limit=40&ts=%s&apikey=%s&hash=%s' % (ts, PUBLIC_KEY, hash_value)
    chars = requests.get(request_url)
    results = chars.json()
    results_lis = results.get('data').get('results')
    character_lis = process_results(results_lis)
    return character_lis

def get_characters_by_name(name):
    global PUBLIC_KEY, hash_value, ts
    request_url = 'https://gateway.marvel.com/v1/public/characters?name=%s&ts=%s&apikey=%s&hash=%s' % (name, ts, PUBLIC_KEY, hash_value)
    specific_char = requests.get(request_url)
    results = specific_char.json()
    results_char = results.get('data').get('results')
    return results_char

def get_character_by_id(id):
    global PUBLIC_KEY, hash_value, ts

    request_url = 'https://gateway.marvel.com/v1/public/characters/%s?&ts=%s&apikey=%s&hash=%s' % (id, ts, PUBLIC_KEY, hash_value)
    specific_char = requests.get(request_url)
    results = specific_char.json()
    results_char = results.get('data').get('results')
    return results_char

def get_comics_by_charid(id):
    global PUBLIC_KEY, hash_value, ts
    request_url = 'http://gateway.marvel.com/v1/public/characters/%s/comics?&ts=%s&apikey=%s&hash=%s' %(id, ts, PUBLIC_KEY, hash_value)
    comic_json = requests.get(request_url)
    comic_res = comic_json.json().get('data').get('results')
    comic_results = process_comics(comic_res)
    return comic_results

def get_all_comics():
    global PUBLIC_KEY, hash_value, ts
    request_url = 'http://gateway.marvel.com/v1/public/comics?orderBy=-modified&limit=40&ts=%s&apikey=%s&hash=%s' % (ts, PUBLIC_KEY, hash_value)
    comic_json = requests.get(request_url)
    comic_res = comic_json.json().get('data').get('results')
    comic_results = process_comics(comic_res)
    return comic_results

def get_comic_by_id(id):
    global PUBLIC_KEY, hash_value, ts

    request_url = 'http://gateway.marvel.com/v1/public/comics/%s?&ts=%s&apikey=%s&hash=%s' % (id, ts, PUBLIC_KEY, hash_value)
    specific_comic = requests.get(request_url)
    results = specific_comic.json()
    results_comic = results.get('data').get('results')
    return results_comic

def process_comics(items):
    comic_res = []
    for item in items:
        id = item.get('id')
        title = item.get('title')
        description = item.get('description')
        page_cnt = item.get('pageCount')
        thumb = item.get('thumbnail').get('path')
        price = item.get('prices')[0].get('price')
        
        comic_obj = Comic(id, title, description, page_cnt, thumb, price)
        comic_res.append(comic_obj)
    return comic_res


def process_results(items):
    character_res = []
    for item in items:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        image_url = item.get('thumbnail').get('path')
        comics = item.get('comics').get('available')

        character_obj = Character(id, name, description, image_url, comics)
        character_res.append(character_obj)
    return character_res

#for debugging
# print(r.url)
# print(r.json())
# results_list = r.json().get('data').get('results')

# print(results_list)
# for result in results_list:
#     print(result.get('title'))