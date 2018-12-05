import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Prepared by Erik Brousseau

class comments_CRUD_ATS(unittest.TestCase):
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

        # add comment
        driver.get("http://ebrousseau.pythonanywhere.com/admin/")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[3]/table/tbody/tr/th/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
        elem = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/form/div/fieldset[1]/div[1]/div/div/select/option[5]").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_object_pk")
        elem.send_keys("15")
        time.sleep(2)
        elem = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/form/div/fieldset[1]/div[3]/div/div/select/option[2]").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_user")
        elem.send_keys("1")
        time.sleep(2)
        elem = driver.find_element_by_id("id_user_name")
        elem.send_keys("admin")
        time.sleep(2)
        elem = driver.find_element_by_id("id_user_email")
        elem.send_keys("pythonrocks225@gmail.com")
        elem = driver.find_element_by_xpath("//*[@id='id_comment']")
        elem.send_keys("another test comment")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset[3]/div[1]/div/p/span[1]/a[1]").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset[3]/div[1]/div/p/span[2]/a[1]").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(4)

        #edit comment
        driver.get("http://ebrousseau.pythonanywhere.com/admin/django_comments/comment/")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='id_comment']")
        elem.send_keys(" another test comment 2")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(2)

        #Delete comment
        driver.get("http://ebrousseau.pythonanywhere.com/admin/django_comments/comment/")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click()
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
        time.sleep(2)



