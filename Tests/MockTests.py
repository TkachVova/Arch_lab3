__author__ = 'vladymyr'

import PizzaHutRestServer

import CreatePizzaHutDb
import unittest
import mock
import json
import bottle


class Tests(unittest.TestCase):

    @mock.patch('CreatePizzaHutDb.add', return_value=0)
    def test_func(self, func_mock):
        result = PizzaHutRestServer.test(2, 3)
        #func_mock.assert_called_once_with(2, 3)
        print(result)
        self.assertEqual(result, 0)


    @mock.patch('CreatePizzaHutDb.GetPizzas', return_value=[{u'price': 6.23, u'_id': '55468982777d472c76caa30e', u'id': 1, u'name': u'Americana', u'ingridients': u'souce, cheese, bacon'},
        {u'price': 5.0, u'_id': '55468982777d472c76caa30f', u'id': 2, u'name': u'Mushrooms', u'ingridients': u'souce, cheese, bacon, mushrooms'}])
    def test_pizzalist(self, func_mock):
        result = PizzaHutRestServer.pizzas_list()
        self.assertEqual({'pizzas': [{'price': 6.23, 'ingridients': u'souce, cheese, bacon', 'id': 1, 'name': u'Americana'}, {'price': 5.0, 'ingridients': u'souce, cheese, bacon, mushrooms', 'id': 2, 'name': u'Mushrooms'}]}, result)
        #print(result)

    @mock.patch('CreatePizzaHutDb.GetPizza', return_value={u'price': 6.23, u'_id': '55468982777d472c76caa30e', u'id': 1, u'name': u'Americana', u'ingridients': u'souce, cheese, bacon'})
    def test_Pizza_Show(self, func_mock):
        result = PizzaHutRestServer.pizza_show(1)
        self.assertEqual(result, {"pizza": {u'price': 6.23, u'id': 1, u'name': u'Americana', u'ingridients': u'souce, cheese, bacon'}})


    @mock.patch('CreatePizzaHutDb.RemovePizza', return_value=0)
    def test_Pizza_Delete(self, func_mock):
        result = PizzaHutRestServer.pizza_delete(1)
        self.assertEqual(result, {"success": True})



