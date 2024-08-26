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


@app.get("/total_pokemons")
def get_total_pokemons() -> dict : 
    return {"total" : len(pokemon_dict) }
