import pymongo 
from pymongo  import MongoClient

client = MongoClient(host="localhost", port=27017)

# ou bien 

db_uri = "mongodb+srv://Thomas:regliss22@cluster0.uc5d5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(db_uri)
db = client["myFirstDatabase"]
Collection = db["Users"]
# affichage un objet
print(client.list_database_names())