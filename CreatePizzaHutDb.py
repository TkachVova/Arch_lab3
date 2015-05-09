__author__ = 'vladymyr'
from pymongo import MongoClient
from bson.objectid import ObjectId



client = MongoClient('localhost', 27017)
db = client.PizzaHutDb
collection = db.PizzaCollection

def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})



pizzas = db.pizzas
new_pizzas =[
    {"id": 1,
       "name": "Americana",
       "ingridients": "souce, cheese, bacon",
        "price": 6.23},
    {"id": 2,
       "name": "Mushrooms",
       "ingridients": "souce, cheese, bacon, mushrooms",
        "price": 5.00},
    {"id": 3,
       "name": "5 cheeses",
       "ingridients": "souce, cheese",
        "price": 10.00},
    {"id": 4,
       "name": "Texas",
       "ingridients": "red pepper, souce, cheese, bacon",
        "price": 4.23},
    {"id": 5,
       "name": "Chicken",
       "ingridients": "chicken, souce, cheese, bacon",
        "price": 9.00},
    {"id": 6,
       "name": "Vegatable",
       "ingridients": "souce, cheese, vegatables",
        "price": 1.23},
    {"id": 7,
       "name": "Havai",
       "ingridients": "pine apple, souce, cheese, bacon",
        "price": 8.23}
        ]

#use 1 time when creating db
def CreatePizzas():
    pizzas.insert_many(new_pizzas)

def GetPizzas():
    return pizzas.find()

def GetPizza(id):
    return pizzas.find_one({"id":id})

def RemovePizza(id):
    pizzas.delete_one({"id":id})
    print("Deleted "+ str(id))

def AddPizza(pizza):
    pizzas.insert_one(pizza)

def UpdatePizza(id, pizza):
    pizzas.replace_one({"id":id}, pizza)

def add(x, y):
    return x + y


#run 1 time
#CreatePizzas()


for i in GetPizzas():
    print(i)
print (pizzas.count())
print(db.collection_names(include_system_collections=False))
