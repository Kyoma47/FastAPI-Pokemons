import json 
from classes import Pokemon

# Chargement des pokemons : json => python list
with open("pokemons.json", "r") as file :
    pokemon_list = json.load( file )

# Tri de la liste par "id" (facultatif) : 
pokemon_list = sorted( pokemon_list, key=lambda x: x['id'], reverse=False )

# list => dict : indexé par "id"
pokemon_dict = {
    k+1 : v  for k,v in enumerate(pokemon_list)
}




print(pokemon_dict)