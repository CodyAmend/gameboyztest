import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class coupon_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\8380tests\myvenv\Scripts\chromedriver.exe")

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://ebrousseau.pythonanywhere.com/admin/login/?next=/admin/")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/input").click()
        time.sleep(2)
        assert "logged in"
        #Create
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_code")
        elem.send_keys("1111")
        elem = driver.find_element_by_xpath( "/html/body/div[1]/div[3]/div/form/div/fieldset/div[2]/div/p/span[1]/a[1]").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[2]/div/p/span[2]/a[1]").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_valid_to_0")
        elem.send_keys("2018-12-31")
        elem = driver.find_element_by_id("id_valid_to_1")
        elem.send_keys("12:00:00")
        elem = driver.find_element_by_id("id_discount")
        elem.send_keys("15")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/label").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(2)
        #Edit
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_discount")
        elem.clear()
        elem.send_keys("25")
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(1)
        #Delete
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click()
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a[3]").click()
        time.sleep(1)
        assert "logged out"

        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()


