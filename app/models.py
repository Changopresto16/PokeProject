from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    pokemon = db.relationship('Pokemon', secondary='user_pokemon')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    ability = db.Column(db.String(200))
    img_url = db.Column(db.String(200))
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)

    def __init__(self, name, hp, defense, attack, img_url, ability):
        self.name = name
        self.ability = ability
        self.img_url = img_url
        self.hp = hp
        self.attack = attack
        self.defense = defense

class UserPokemon(db.Model):
    __table_name__ = 'user_pokemon'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    pokemon_id = db.Column(db.Integer, ForeignKey('pokemon.id'))

    def __init__(self, user_id, pokemon_id):
        self.pokemon_id = pokemon_id
        self.user_id = user_id

