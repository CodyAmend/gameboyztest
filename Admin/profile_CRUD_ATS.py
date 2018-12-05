import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Prepared by Erik Brousseau

class profile_CRUD_ATS(unittest.TestCase):
    # this sets up the location of the chrome driver
    def setUp(self):
        self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")

    def test_Admin(self):
        # admin login
        driver = self.driver
        driver.maximize_window()
        driver.get("http://ebrousseau.pythonanywhere.com/admin")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        time.sleep(2)
        elem.send_keys("admin")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("eb708199")
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(3)
        driver.get("http://ebrousseau.pythonanywhere.com/admin")

        #Create Profile
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[6]/table/tbody/tr[3]/th/a").click()
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[1]/div/div/select/option[14]").click()
        elem = driver.find_element_by_id("id_phone_number")
        time.sleep(2)
        elem.send_keys("402-657-1789")
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[3]/div/span[1]/a[1]").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(2)

        #Update Profile
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        elem = driver.find_element_by_id("id_phone_number")
        time.sleep(2)
        elem.clear()
        elem.send_keys("402-829-4567")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(2)

        #Delete Profile
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click()
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
        time.sleep(2)




