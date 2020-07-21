from ..requests import get_characters, get_character_by_id
from flask import render_template, redirect, url_for
from . import main

@main.route('/')
def index():
    title= 'Home | Marvel'
    chars = get_characters()
    return render_template('main/index.html', chars=chars)

@main.route('/char/<int:id>')
def each_char(id):
    character = get_character_by_id(id)[0]
    title = character.get('name')
    return render_template('main/each_char.html', character=character)