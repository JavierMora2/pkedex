from bson import ObjectId
from app import mongo
from app.models.super_clase import SuperClass

class PokemonFavorites(SuperClass):
   def __init__(self):
        super().__init__("pokemon_favorites")
   
   def update(self, object_id, data):
       raise NotImplementedError("Los pokemones no se pueden actualizar")
   
   def find_by_id(self, object_id):
       raise NotImplementedError("Los pokemones no se pueden encontrar de manera individual")
   
   def find_all(self):
       data = self.collection.find({"user_id": ObjectId(userid)})
       return data
   