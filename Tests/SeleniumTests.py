__author__ = 'vladymyr'

import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
import time

class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()


    def test_clients_do_tasks(self):
        driver = self.driver
        driver.get("localhost:8080")

        main_window = driver.current_window_handle



    def tearDown(self):
        self.driver.close()
