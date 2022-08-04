from app import app
from app.models import Pokemon, db
from flask import render_template, request, Blueprint
from app.forms import PokemonSearchForm
import requests


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=["GET", "POST"])
def search_pokemon():
    form = PokemonSearchForm()
    my_dict = {}
    print(my_dict)
    if request.method == "POST":
        print('pikachu')
        poke_name = form.name.data.lower()
        name = Pokemon.query.filter(Pokemon.name==poke_name).first()
        print(name)
        url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
        res = requests.get(url)
        if name:
            data = res.json()
            user_pokemon = []
            my_dict = {
                'name': data['name'],
                'ability': data['abilities'][0]['ability']['name'],
                'img_url': data['sprites']['front_shiny'],
                "hp": data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'defense': data['stats'][2]['base_stat']
            }

            # print(my_dict)
            # return render_template('searchpokemon.html', form = form, pokemon = my_dict)

            name = data['name']
            ability = data['abilities'][0]['ability']['name']
            img_url = data['sprites']['front_shiny']
            hp = data['stats'][0]['base_stat']
            attack = data['stats'][1]['base_stat']
            defense = data['stats'][2]['base_stat']
            user_pokemon.append(my_dict)
            pokemon = Pokemon(name, hp, defense, attack, img_url, ability)

            return render_template('searchpokemon.html', form=form, pokemon=my_dict)

        if res.ok:
            data = res.json()
            user_pokemon = []
            my_dict = {
                'name': data['name'],
                'ability': data['abilities'][0]['ability']['name'],
                'img_url': data['sprites']['front_shiny'],
                "hp": data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'defense': data['stats'][2]['base_stat']
            }

            # print(my_dict)
            # return render_template('searchpokemon.html', form = form, pokemon = my_dict)

            name = data['name']
            ability = data['abilities'][0]['ability']['name']
            img_url = data['sprites']['front_shiny']
            hp = data['stats'][0]['base_stat']
            attack = data['stats'][1]['base_stat']
            defense = data['stats'][2]['base_stat']
            user_pokemon.append(my_dict)
            pokemon = Pokemon(name, hp, defense, attack, img_url, ability)
            db.session.add(pokemon)
            db.session.commit()

            return render_template('searchpokemon.html', form=form, pokemon=my_dict)

    return render_template('searchpokemon.html', form=form, pokemon=my_dict)
