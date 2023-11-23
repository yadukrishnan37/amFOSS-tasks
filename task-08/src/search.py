import requests
from PySide6.QtWidgets import QMessageBox

def search_pokemon(pokemon_name):
    if not pokemon_name:
        QMessageBox.warning(None, "Warning", "Please enter a Pokemon name.")
        return None

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()

        abilities = pokemon_data['abilities']
        ability_names = [ability['ability']['name'] for ability in abilities]
        abilities_text = ", ".join(ability_names)

        types = pokemon_data['types']
        type_names = [type_entry['type']['name'] for type_entry in types]
        types_text = ", ".join(type_names)

        stats = pokemon_data['stats']
        stats_text = "Stats:\n"
        for stat_entry in stats:
            stat_name = stat_entry['stat']['name']
            base_stat = stat_entry['base_stat']
            stats_text += f"{stat_name}: {base_stat}\n"

        # Accessing artwork
        art = pokemon_data['sprites']['other']['official-artwork']['front_default']

        return abilities_text, types_text, stats_text, art

    else:
        QMessageBox.critical(None, "Error", "Failed to fetch data from the API.")
        return None
