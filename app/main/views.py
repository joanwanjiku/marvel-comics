from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User
from .form import UpdateProfile
from .. import db,photos
from ..requests import get_characters, get_character_by_id
from . import main


@main.route('/')
def index():
    title= 'Home | Marvel'
    return render_template('main/index.html' )

@main.route('/characters')
def all_characters():
    chars = get_characters()
    return render_template('main/character.html', chars=chars) 

@main.route('/char/<int:id>')
def each_char(id):
    character = get_character_by_id(id)[0]
    title = character.get('name')
    return render_template('main/each_char.html', character=character)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form)


@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))



