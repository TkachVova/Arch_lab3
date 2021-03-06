__author__ = 'vladymyr'
import json
from bottle import route, run, request, template, static_file
from CreatePizzaHutDb import GetPizzas, GetPizza, RemovePizza, AddPizza, UpdatePizza
import CreatePizzaHutDb
import bottle

@route('/')
def default():
    return template('default')

#@route('/home')
#def home():
#    print('inside home')
#    return static_file('home.html', 'static/templates')

@route('/pizzas/', method="GET")
def pizzas_list():
    pizzaList = []
    for p in CreatePizzaHutDb.GetPizzas():
        pizza = {}
        pizza["id"] = p["id"]
        pizza["name"] = p["name"]
        pizza["ingridients"] = p["ingridients"]
        pizza["price"] = p["price"]
        pizzaList.append(pizza)
    return {"pizzas":pizzaList}


@route('/pizzas/', method="POST")
def pizzas_add():
    xml = json.loads(bottle.request.body.read( ))
    print (xml)
    CreatePizzaHutDb.AddPizza(xml)
    return {"success": True}

@route('/pizzas/<id>', method='GET')
def pizza_show( id ):
    i = int(id)
    p = CreatePizzaHutDb.GetPizza(i)
    pizza = {}
    pizza["id"] = p["id"]
    pizza["name"] = p["name"]
    pizza["ingridients"] = p["ingridients"]
    pizza["price"] = p["price"]
    return {"pizza" : pizza}

@route('/pizzas/<id>', method='DELETE' )
def pizza_delete( id="1" ):
    i = int(id)
    CreatePizzaHutDb.RemovePizza(i)
    return { "success" : True}

@route('/pizzas/<id>', method='PUT')
def pizza_save( id="1" ):
    i = int(id)
    print(id)
    xml = json.loads(request.body.read())
    UpdatePizza(i, xml)
    print (xml)
    return { "success": True}


def test(a, b):
    return CreatePizzaHutDb.add(a,b)


# Static Routes
@route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@route('/<filename:re:.*\.html>')
def templates(filename):
    return static_file(filename, root='static/templates')

@route('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

run(host='localhost', port=8080, debug=True)


