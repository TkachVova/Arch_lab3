__author__ = 'vladymyr'

from PizzaHutRestServer import test, pizzas_list

import CreatePizzaHutDb
import unittest
import mock

class Tests(unittest.TestCase):
    #@patch.object('CreatePizzaHutDb' ,'GetPizzas')
    def testPizzasList(self):
        #self.maxDiff = None
        #with patch.object('CreatePizzaHutDb.GetPizzas', return_value = [{u'price': 6.23, u'_id': '55468982777d472c76caa30e', u'id': 1, u'name': u'Americana', u'ingridients': u'souce, cheese, bacon'},
        #    {u'price': 6.23, u'_id': '55468982777d472c76caa30e', u'id': 1, u'name': u'Americana', u'ingridients': u'souce, cheese, bacon'}]) as getpizzasMock:
        x = pizzas_list()
        print(x)
            #self.assertEqual({"pizzas": [{"price": 6.23, "ingridients": "souce, cheese, bacon", "id": 1, "name": "Americana"}, {"price": 5.0, "ingridients": "souce, cheese, bacon, mushrooms", "id": 2, "name": "Mushrooms"}]},
            #                 pizzas_list())

    @mock.patch('CreatePizzaHutDb.plus')
    def tetsTest(self, m):
        m.return_value = 0
        x = test(1,2)
        print(x)
