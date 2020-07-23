from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash

class Character:
    def __init__(self, id, name, description, img_url, comics):

        self.id = id
        self.name = name
        self.description = description
        self.path = img_url
        self.comics = comics
# {
#     'id': 1308, 
#     'digitalId': 0, 
#     'title': 'Marvel Age Spider-Man Vol. 2: Everyday Hero (Digest)', 
#     'issueNumber': 0, 'variantDescription': '', 'description': '"The Marvel Age of Comics continues! This time around, Spidey meets his match against such classic villains as Electro and the Lizard, and faces the return of one of his first foes: the Vulture! Plus: Spider-Man vs. the Living Brain, Peter Parker\'s fight with Flash Thompson, and the wall-crawler tackles the high-flying Human Torch!"', 
#     'modified': '2018-01-22T15:42:11-0500', 'isbn': '0-7851-1451-3', 'upc': '5960611451-00111', 'diamondCode': '', 'ean': '', 'issn': '', 'format': 'Digest', 
#     'pageCount': 96, 'textObjects': [{'type': 'issue_solicit_text', 'language': 'en-us', 'text': '"The Marvel Age of Comics continues! This time around, Spidey meets his match against such classic villains as Electro and the Lizard, and faces the return of one of his first foes: the Vulture! Plus: Spider-Man vs. the Living Brain, Peter Parker\'s fight with Flash Thompson, and the wall-crawler tackles the high-flying Human Torch!"'}], 
#     }
class Comic:
    def __init__(self, id, title, description, page_count, thumbnail, price):
        self.id = id
        self.title = title
        self.description = description
        self.page_count = page_count
        self.thumbnail = thumbnail
        self.price = price

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(150),default ='default.png')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    favourites = db.relationship('Favourite', backref = 'user', lazy='dynamic')
    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

# {'id': 1009351, 'name': 'Hulk', 'description': 
# 'Caught in a gamma bomb explosion while trying to save the life of a teenager, Dr. Bruce Banner was transformed into the incredibly powerful creature called the Hulk. An all too often misunderstood hero, the angrier the Hulk gets, the stronger the Hulk gets.', 'modified': '2020-04-04T19:04:20-0400', 
# 'thumbnail': {'path': 'http://i.annihil.us/u/prod/marvel/i/mg/5/a0/538615ca33ab0', 'extension': 'jpg'}, 
# 'resourceURI': 'http://gateway.marvel.com/v1/public/characters/1009351', 
# 'comics': {'available': 1660, 'collectionURI': 'http://gateway.marvel.com/v1/public/characters/1009351/comics'}}
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    char_id = db.Column(db.Integer)
    char_name = db.Column(db.String)
    char_path = db.Column(db.String)
    title = db.Column(db.String)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_comments(cls, char_id):
        comments = cls.query.filter_by(char_id = char_id)
        return comments

class Favourite(db.Model):
    __tablename__ = 'favourites'
    id = db.Column(db.Integer, primary_key=True)
    char_id = db.Column(db.Integer)
    char_name = db.Column(db.String)
    char_path = db.Column(db.String)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_fav(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_favourites(cls, id):
        favourites = cls.query.filter_by(user_id = id).all()
        return favourites

