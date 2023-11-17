from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_pokemon_info(pokemon_name):
    # URL da PokeAPI para obter informações do Pokémon
    pokeapi_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'

    response = requests.get(pokeapi_url)

    if response.status_code == 200:
        data = response.json()
        pokemon_name = data['name']
        types = [t['type']['name'] for t in data['types']]

        # Obtém a URL da imagem de alta qualidade do Pokémon da PokéAPI/SPRITES
        images_url = data['sprites']['other']['official-artwork']['front_default']

        return pokemon_name, types, images_url
    else:
        return None, None, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    pokemon_name = request.form['pokemon_name']
    pokemon_name, types, pokemon_image = get_pokemon_info(pokemon_name)

    return render_template('index.html', pokemon_name=pokemon_name, types=types, pokemon_image=pokemon_image)

if __name__ == '__main__':
    app.run(debug=True)