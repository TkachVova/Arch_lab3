__author__ = 'vladymyr'

import unittest
from CreatePizzaHutDb import CountPizzas, GetPizzas
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("localhost:8080")
        self.testPizzaId = -1

    def test_adding(self):
        driver = self.driver
        amount_of_pizzas_before_adding = CountPizzas()
        addkey = driver.find_element_by_id("addpizza")
        addkey.click()
        pizzaname = driver.find_element_by_id("pizzaname").send_keys("TestPizza")
        pizzaingr = driver.find_element_by_id("pizzaingridients").send_keys("TestIngridients")
        pizzaprice = driver.find_element_by_id("pizzaprice").send_keys("111")
        submitadd = driver.find_element_by_id("submitadd").click()
        try:
             WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

             alert = driver.switch_to_alert()
             alert.accept()
             print "alert accepted"
        except TimeoutException:
            print "no alert"
        assert amount_of_pizzas_before_adding + 1, CountPizzas()
        pizzas = GetPizzas()
        pizza = ""
        for i in pizzas:
            pizza = i
        self.testPizzaId = pizza["id"]
        assert pizza["name"], "TestPizza"
        assert pizza["ingridients"], "TestIngridients"
        assert pizza["price"], "111"

    def test_delete(self):
        driver = self.driver
        deleteBut = driver.find_elements_by_xpath(".//*[@id='del']")
        lastPizzaNumber = CountPizzas()
        deleteBut[lastPizzaNumber - 1].click()
        try:
             WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

             alert = driver.switch_to_alert()
             alert.accept()
             print "alert accepted"
        except TimeoutException:
            print "no alert"

        assert lastPizzaNumber - 1, CountPizzas()
        pizzas = GetPizzas()
        for i in pizzas:
            if i["id"] == self.testPizzaId:
                assert True, False

    def tearDown(self):
        self.driver.close()
