__author__ = 'vladymyr'
import json
from bottle import route, run, request, template, static_file
from CreatePizzaHutDb import GetPizzas, GetPizza, RemovePizza

@route('/')
def default():
    return template('default')

#@route('/home')
#def home():
#    print('inside home')
#    return static_file('home.html', 'static/templates')

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
    i = int(id)
    RemovePizza(i)
    return { "success" : False, "error" : "delete not implemented yet" }

@route('/pizzas/<id>', method='PUT')
def pizza_save( id="1" ):
    xml = request.forms.get( "xml" )
    if "" != id and "" != xml:
        return { "success" : True, "path" : id }
    else:
        return { "success" : False, "error" : "save called without a filename or content" }


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


