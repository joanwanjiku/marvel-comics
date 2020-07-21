class Character:
    def __init__(self, id, name, description, img_url, comics):

        self.id = id
        self.name = name
        self.description = description
        self.path = img_url
        self.comics = comics

# {'id': 1009351, 'name': 'Hulk', 'description': 
# 'Caught in a gamma bomb explosion while trying to save the life of a teenager, Dr. Bruce Banner was transformed into the incredibly powerful creature called the Hulk. An all too often misunderstood hero, the angrier the Hulk gets, the stronger the Hulk gets.', 'modified': '2020-04-04T19:04:20-0400', 
# 'thumbnail': {'path': 'http://i.annihil.us/u/prod/marvel/i/mg/5/a0/538615ca33ab0', 'extension': 'jpg'}, 
# 'resourceURI': 'http://gateway.marvel.com/v1/public/characters/1009351', 
# 'comics': {'available': 1660, 'collectionURI': 'http://gateway.marvel.com/v1/public/characters/1009351/comics'}}
