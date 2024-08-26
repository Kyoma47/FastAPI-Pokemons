from dataclasses import asdict
import json 
from classes import Pokemon
from fastapi import FastAPI, Path, HTTPException

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

#========================================
#  GET 
#========================================
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

# Récuperer un seul pokemon :
@app .get("/pokemon/{id}")
def get_pokemon_by_id(id : int = Path(ge=1) ) -> Pokemon : # Negative id => 422 Unprocessable Entity
#def get_pokemon_by_id(id : int = Path(ge=1, lt=150) ) -> Pokemon : 
    if id not in pokemon_dict :
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas !")
    return Pokemon(**pokemon_dict[id])


#========================================
#  POST 
#========================================
# Créer un Nouveau Pokemon :
@app.post("/pokemon")
def create_pokemon( pokemon : Pokemon ) -> Pokemon :
    if pokemon.id in pokemon_dict :
        raise HTTPException(status_code=404, detail="Le pokemon {pokemon.id} existe déjà.")
    pokemon_dict[pokemon.id] = asdict( pokemon ) 
    return pokemon

#========================================
#  PUT 
#========================================
# Modifier un pokemon :
@app.post("/pokemon/{id}")
def update_pokemon(pokemon: Pokemon, id: int = Path(ge=1) ) -> Pokemon :
    if pokemon.id not in pokemon_dict :
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas !")
    pokemon_dict[id] = asdict( pokemon )
    return pokemon