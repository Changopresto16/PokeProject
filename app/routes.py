from app import app
from flask import render_template, request
import requests 
from app.forms import PokemonSearchForm


@app.route('/')
def index():
    return render_template('index.html')    

@app.route('/search', methods =  ["GET","POST"])
def searchPokemon():
    form= PokemonSearchForm()
    my_dict = {}
    if request.method == "POST":
        poke_name = form.name.data



        url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
        res = requests.get(url)
        if res.ok:
            data = res.json()
            my_dict = {
                'name': data['name'],
                'ability': data['abilities'][0]['ability']['name'],
                'img_url': data['sprites']['front_shiny'],
                "hp": data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'defense': data['stats'][2]['base_stat']
            }
  
    return render_template('searchpokemon.html', form=form, pokemon = my_dict)