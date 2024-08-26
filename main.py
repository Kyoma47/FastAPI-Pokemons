import json 
from classes import Pokemon
from fastapi import FastAPI

# Chargement des pokemons : json => python list
with open("pokemons.json", "r") as file :
    pokemon_list = json.load( file )

# Tri de la liste par "id" (facultatif) : 
pokemon_list = sorted( pokemon_list, key=lambda x: x['id'], reverse=False )

# list => dict : indexé par "id"
pokemon_dict = {
    k+1 : v  for k,v in enumerate(pokemon_list)
}

app = FastAPI()

# Nombre de pokemons : 
@app.get("/total_pokemons")
def get_total_pokemons() -> dict : 
    return {"total" : len(pokemon_dict) }

# Liste des pokemons :
@app.get("/pokemons")
def get_all_pokemons() -> list[Pokemon] :
    response = [] 
    for id in pokemon_dict : 
        response.append( Pokemon( **pokemon_dict[id] ) )
    return response