import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class coupon_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\python\gameboyz\myvenv\Scripts\chromedriver.exe")

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
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_code")
        elem.send_keys("1234")
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[2]/div/p/span[1]/a[1]").click()
        elem = driver.find_element_by_xpath( "/html/body/div[1]/div[3]/div/form/div/fieldset/div[2]/div/p/span[2]/a[1]").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_valid_to_0")
        elem.send_keys("2018-12-31")
        elem = driver.find_element_by_id("id_valid_to_1")
        elem.send_keys("12:00:00")
        elem = driver.find_element_by_id("id_discount")
        elem.send_keys("10")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/label").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/header/div[1]/nav/ul/li[2]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/a[2]").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/main/div[1]/form/input[3]").click()
        elem = driver.find_element_by_id("id_code")
        elem.send_keys("1234")
        elem = driver.find_element_by_xpath("/html/body/div/form/input[2]").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/p[2]/a[2]").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Cody")
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Amend")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("camend@unomaha.edu")
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("4026571789")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("123 Somewhere St.")
        elem = driver.find_element_by_id("id_postal_code")
        elem.send_keys("68102")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/main/form/p[8]/input").click()
        time.sleep(3)
        driver.switch_to.frame(0)
        elem = driver.find_element_by_xpath("//input[@id='credit-card-number']")
        elem.clear()
        elem.send_keys("4111 1111 1111 1111")
        driver.switch_to.default_content()
        driver.switch_to.frame(1)
        elem = driver.find_element_by_id("cvv")
        elem.clear()
        elem.send_keys("123")
        driver.switch_to.default_content()
        driver.switch_to.frame(2)
        elem = driver.find_element_by_id("expiration")
        elem.clear()
        elem.send_keys("1220")
        driver.switch_to.default_content()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/form/input[3]").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/header/div[1]/nav/ul/span/div/li[1]/a").click()
        time.sleep(2)

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()