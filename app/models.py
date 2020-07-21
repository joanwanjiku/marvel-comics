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

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(150),default ='default.png')
    

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
