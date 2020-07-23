from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User, Comment, Favourite
from .form import UpdateProfile
from .. import db,photos
from ..requests import get_characters, get_character_by_id, get_characters_by_name, get_comics_by_charid, get_all_comics, get_comic_by_id
from . import main


@main.route('/')
def index():
    title= 'Home | Marvel'

    return render_template('main/index.html')

@main.route('/characters')
def all_characters():
    character_search = request.args.get('char_search')
    if character_search:
        return redirect(url_for('.search_result', char_name=character_search))
    chars = get_characters()
    return render_template('main/character.html', chars=chars) 

@main.route('/comics')
def all_comics():
    comics = get_all_comics()
    title= 'Comics'
    return render_template('main/comic.html', comics = comics, title=title)

@main.route('/results/<char_name>')
def search_result(char_name):
    result = get_characters_by_name(char_name)[0]
    return render_template('main/search_result.html', result=result)

@main.route('/<int:id>/comics')
def char_comics(id):
    character_comics = get_comics_by_charid(id)

    return render_template('main/character_comics.html', character_comics = character_comics)

@main.route('/char/<int:id>')
def each_char(id):
    character = get_character_by_id(id)[0]
    comments = Comment.get_all_comments(id)
    title = character.get('name')
    return render_template('main/each_char.html', character=character, comments=comments)

@main.route('/comic/<int:id>')
def each_comic(id):
    comic = get_comic_by_id(id)[0]
    title = 'Comc'
    return render_template('main/each_comic.html', comic=comic, title=title)


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    print(user.id)
    favourites = Favourite.get_favourites(user.id)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, favourites=favourites)

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
        return redirect(url_for('main.profile',name = name))
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

@main.route('/char/<int:char_id>/comment', methods=['POST', 'GET'])
@login_required
def char_comment(char_id):
    character = get_character_by_id(char_id)[0]
    print(character.get('id'))
    comments = Comment.get_all_comments(char_id)
    if request.method== 'POST':        
        title = request.form['title']
        content = request.form['content']
        new_comment = Comment(
            char_id = character.get('id'),
            char_name = character.get('name'),
            char_path = character.get('thumbnail').get('path'),
            title = title,
            content = content,
            user=current_user
            )
        new_comment.save_comment()
        return redirect(url_for('main.each_char', id = char_id))
    return render_template('main/each_char.html', character=character, comments=comments)
    
@main.route('/char/<int:id>/favourite/')
@login_required
def favourite(id):
    character = get_character_by_id(id)[0]
    comments = Comment.get_all_comments(id)

    fav_char = Favourite(
        char_id = character.get('id'),
        char_name = character.get('name'),
        char_path = character.get('thumbnail').get('path'),
        user = current_user
    )
    fav_char.save_fav()
    return redirect(url_for('main.each_char', id=character.get('id')))




