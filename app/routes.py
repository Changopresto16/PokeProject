from nis import cat
from app import app
from app.models import Pokemon, db, UserPokemon
from flask import redirect, render_template, request, Blueprint, flash 
from app.forms import PokemonSearchForm, CatchForm
from flask_login import current_user, login_required

import requests


@app.route('/')
def index():
    if current_user.is_authenticated:
        pokemon = current_user.pokemon
    return render_template('index.html', pokemon=pokemon)



@app.route('/search', methods=["GET", "POST"])
def search_pokemon():
    form = PokemonSearchForm()
    catch = CatchForm()
    my_dict = {}
    print(my_dict)
    if request.method == "POST":
        poke_name = form.name.data.lower()
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

            
            name = data['name']
            ability = data['abilities'][0]['ability']['name']
            img_url = data['sprites']['front_shiny']
            hp = data['stats'][0]['base_stat']
            attack = data['stats'][1]['base_stat']
            defense = data['stats'][2]['base_stat']
            user_pokemon.append(my_dict)
            pokemon = Pokemon(name, hp, defense, attack, img_url, ability)

            return render_template('searchpokemon.html', form=form, pokemon=my_dict, catch=catch)

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

            return render_template('searchpokemon.html', form=form, pokemon=my_dict, catch=catch)

    return render_template('searchpokemon.html', form=form, pokemon=my_dict, catch=catch)

@app.route('/catch/<name>', methods = ['POST'])
@login_required 
def catch(name):
    catch = CatchForm()
    form = PokemonSearchForm()
    pokemon = Pokemon.query.filter(Pokemon.name==name).first()
    user_pokemon = UserPokemon(current_user.id, pokemon.id)
    db.session.add(user_pokemon)
    db.session.commit()
    flash(f"You Caught {pokemon.name}!", 'success')
    return redirect("/")




