import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Prepared by Erik Brousseau and John Gombas

class misc_scripts(unittest.TestCase):
    # this sets up the location of the chrome driver
    def setUp(self):
        self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")

    def test_misc_scripts(self):

        driver = self.driver
        driver.maximize_window()
        # homepage (Prepared by John Gombas)

        driver.get("http://ebrousseau.pythonanywhere.com")
        time.sleep(15)

        # About (Prepared by John Gombas)

        driver.get("http://ebrousseau.pythonanywhere.com/About")
        time.sleep(8)

        # contact (Prepared by John Gombas)

        driver.get("http://ebrousseau.pythonanywhere.com/Contact")
        time.sleep(8)

        #JSON Products (Prepared by Erik Brousseau)

        driver.get("http://ebrousseau.pythonanywhere.com/Games/products_json")
        time.sleep(5)

        #JSON Games (Prepared by Erik Brousseau)

        driver.get("http://ebrousseau.pythonanywhere.com/orders/orders_json")
        time.sleep(5)


    def tearDown(self):
        self.driver.close()