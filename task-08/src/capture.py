import os
import requests

def capture_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        official_artwork_url = pokemon_data['sprites']['other']['official-artwork']['front_default']

        directory = "/home/yadukrishnan/Desktop/amFOSS23/Poke-Search/assets/captures/"
        filename = f"{pokemon_name.lower()}_artwork.png"
        full_path = os.path.join(directory, filename)

        response_art = requests.get(official_artwork_url)

        if response_art.status_code == 200:
            os.makedirs(directory, exist_ok=True)
            with open(full_path, "wb") as f:
                f.write(response_art.content)
            return True
        else:
            return False
    else:
        return False
