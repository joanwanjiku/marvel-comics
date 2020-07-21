import time
import json
import hashlib

import requests  # pip install requests to get this library
from .models import Character

PUBLIC_KEY = '2353a342668c6dc1db924a94391f6b7c'
PRIVATE_KEY = '9b3b494ae44984e02239963dbac2b9da60461659'

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
    pass

def get_character_by_id(id):
    global PUBLIC_KEY, hash_value, ts

    request_url = 'https://gateway.marvel.com/v1/public/characters/%s?&ts=%s&apikey=%s&hash=%s' % (id, ts, PUBLIC_KEY, hash_value)
    specific_char = requests.get(request_url)
    results = specific_char.json()
    results_char = results.get('data').get('results')
    return results_char


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