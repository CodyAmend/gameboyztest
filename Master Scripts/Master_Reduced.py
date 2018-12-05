import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#prepared by Jon Gombas

class groupCRUD(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D://School/Python/GameBoyz/Scripts/chromedriver.exe")

    def test_group(self):

        #driver setup

        driver = self.driver
        driver.maximize_window()

        #user signs up & logs in

        driver.get("http://ebrousseau.pythonanywhere.com")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Sign-up")
        elem.click()
        elem = driver.find_element_by_id("id_username")
        elem.clear()
        elem.send_keys("Johny_Test")
        elem = driver.find_element_by_id("id_first_name")
        elem.clear()
        elem.send_keys("Johny")
        elem = driver.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("jgombas@unomaha.edu")
        elem = driver.find_element_by_id("id_password")
        elem.clear()
        elem.send_keys("instructor1a")
        elem = driver.find_element_by_id("id_password2")
        elem.clear()
        elem.send_keys("instructor1a")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//input[@value='Create my account']")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_link_text("log in")
        elem.click()
        elem = driver.find_element_by_id("id_username")
        elem.clear()
        elem.send_keys("Johny_Test")
        elem = driver.find_element_by_id("id_password")
        elem.clear()
        elem.send_keys("instructor1a")
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"

        #edit profile

        driver.get("http://ebrousseau.pythonanywhere.com")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Edit Profile")
        elem.click()
        elem = driver.find_element_by_id("id_last_name")
        elem.clear()
        elem.send_keys("Dude")
        elem = driver.find_element_by_id("id_date_of_birth")
        elem.clear()
        elem.send_keys("1987-05-18")
        time.sleep(3)
        elem = driver.find_element_by_xpath("//input[@value='Save changes']")
        elem.click()
        time.sleep(3)


        #homepage

        driver.get("http://ebrousseau.pythonanywhere.com")
        time.sleep(15)

        #About

        driver.get("http://ebrousseau.pythonanywhere.com/About")
        time.sleep(8)

        #contact

        driver.get("http://ebrousseau.pythonanywhere.com/Contact")
        time.sleep(8)



        #check reviews
        driver.get("http://ebrousseau.pythonanywhere.com/Reviews")
        time.sleep(12)


        # select and purchase game

        driver.get("http://ebrousseau.pythonanywhere.com/Games")
        time.sleep(5)
        driver.get("http://ebrousseau.pythonanywhere.com/1/witcher3/")
        time.sleep(8)
        elem = driver.find_element_by_xpath("//input[@value='Add to cart']")
        elem.click()
        time.sleep(3)

        # select & checkout

        driver.get("http://ebrousseau.pythonanywhere.com/cart/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Checkout")
        elem.click()
        elem = driver.find_element_by_id("id_first_name")
        elem.clear()
        elem.send_keys("Jonathan")
        elem = driver.find_element_by_id("id_last_name")
        elem.clear()
        elem.send_keys("Gombas")
        elem = driver.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("jgombas@unomaha.edu")
        elem = driver.find_element_by_id("id_phone_number")
        elem.clear()
        elem.send_keys("4026571789")
        elem = driver.find_element_by_id("id_address")
        elem.clear()
        elem.send_keys("5024 Maple Street")
        elem = driver.find_element_by_id("id_postal_code")
        elem.clear()
        elem.send_keys("68104")
        elem = driver.find_element_by_id("id_city")
        elem.clear()
        elem.send_keys("Omaha")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//input[@value='Place order']")
        elem.click()
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
        time.sleep(4)
        elem = driver.find_element_by_xpath("//input[@value='Pay']")
        elem.click()
        time.sleep(5)

        #logout
        driver.get("http://ebrousseau.pythonanywhere.com")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Logout")
        elem.click()


        # admin login

        driver.get("http://ebrousseau.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("admin")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("eb708199")
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(3)


        #get orders

        driver.get("http://ebrousseau.pythonanywhere.com/admin")
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/orders/order/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("38")
        elem.click()
        time.sleep(12)

        #get social auth

        driver.get("http://ebrousseau.pythonanywhere.com/admin")
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/social_django/usersocialauth/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("jgombas")
        elem.click()
        time.sleep(12)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()