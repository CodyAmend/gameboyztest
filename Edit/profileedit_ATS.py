import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class profileedit_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\gameboyz2\myvenv\Scripts\chromedriver.exe")

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://ebrousseau.pythonanywhere.com/")
        elem = driver.find_element_by_xpath("/html/body/header/div/nav/ul/span/div/li[2]/a").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem = driver.find_element_by_xpath("/html/body/div/main/div[1]/form/p[3]/input").click()
        time.sleep(5)
        assert "logged in"
        elem = driver.find_element_by_xpath("/html/body/header/div[1]/nav/ul/span/div/li[2]/a").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Royce")
        elem = driver.find_element_by_xpath("/html/body/div/form/p[6]/input").click()
        time.sleep(5)
        assert "save changes"
        elem = driver.find_element_by_xpath("/html/body/header/div[1]/nav/ul/span/div/li[1]/a").click()
        time.sleep(5)
        assert "logged out"

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()
