__author__ = 'vladymyr'
import json
from bottle import route, run, request
from CreatePizzaHutDb import GetPizzas, GetPizza








@route('/pizzas/')
def pizzas_list():
    pizzaList = []
    for p in GetPizzas():
        pizza = {}
        pizza["id"] = p["id"]
        pizza["name"] = p["name"]
        pizza["ingridients"] = p["ingridients"]
        pizza["price"] = p["price"]
        pizzaList.append(pizza)
    return {"pizzas":pizzaList}

@route('/pizzas/<id>', method='GET')
def pizza_show( id ):
    i = int(id)
    p = GetPizza(i)
    pizza = {}
    pizza["id"] = p["id"]
    pizza["name"] = p["name"]
    pizza["ingridients"] = p["ingridients"]
    pizza["price"] = p["price"]
    return {"pizza" : pizza}

@route('/pizzas/<id>', method='DELETE' )
def recipe_delete( id="1" ):
    return { "success" : False, "error" : "delete not implemented yet" }

@route('/pizzas/<id>', method='PUT')
def pizza_save( id="1" ):
    xml = request.forms.get( "xml" )
    if "" != id and "" != xml:
        return { "success" : True, "path" : id }
    else:
        return { "success" : False, "error" : "save called without a filename or content" }


run(host='localhost', port=8080, debug=True)


