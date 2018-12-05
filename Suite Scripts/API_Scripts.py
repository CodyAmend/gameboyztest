import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Prepared by John Gombas, Erik Brousseau, Cody Amend

class API_Scripts(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")

   def test_API_Scripts(self):
       driver = self.driver
       driver.maximize_window()

       #login (Prepared by John Gombas)
       username = "testuser"
       pwd = "eb708199"
       driver.get("http://ebrousseau.pythonanywhere.com")
       elem = driver.find_element_by_xpath("/html/body/header/div/nav/ul/span/div/li[2]/a").click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(username)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)


       # select and purchase game (Prepared by John Gombas)

       driver.get("http://ebrousseau.pythonanywhere.com/Games")
       time.sleep(5)
       driver.get("http://ebrousseau.pythonanywhere.com/3/zelda-breath-wild/")
       time.sleep(5)
       elem = driver.find_element_by_xpath("//input[@value='Add to cart']")
       elem.click()
       time.sleep(3)

       # select & checkout (Prepared by John Gombas)

       driver.get("http://ebrousseau.pythonanywhere.com/cart/")
       time.sleep(3)
       elem = driver.find_element_by_link_text("Checkout")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_first_name")
       elem.clear()
       elem.send_keys("Jonathan")
       time.sleep(2)
       elem = driver.find_element_by_id("id_last_name")
       elem.clear()
       elem.send_keys("Gombas")
       time.sleep(2)
       elem = driver.find_element_by_id("id_email")
       elem.clear()
       elem.send_keys("jgombas@unomaha.edu")
       time.sleep(2)
       elem = driver.find_element_by_id("id_phone_number")
       elem.clear()
       elem.send_keys("4026571789")
       time.sleep(2)
       elem = driver.find_element_by_id("id_address")
       elem.clear()
       elem.send_keys("5024 Maple Street")
       time.sleep(2)
       elem = driver.find_element_by_id("id_postal_code")
       elem.clear()
       elem.send_keys("68104")
       time.sleep(2)
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



       #View Twitch Videos (Prepared by Erik Brousseau)

       driver.get("http://ebrousseau.pythonanywhere.com/")
       elem = driver.find_element_by_xpath("/html/body/header/div[1]/nav/ul/li[3]/a").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='dropdownMenuButton']").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/main/div[2]/div/a[1]").click()
       time.sleep(3)

       #Leaving a Game Comment (Prepared by Erik Brousseau)
       comment = "test comment"
       driver.get("http://ebrousseau.pythonanywhere.com/")
       elem = driver.find_element_by_xpath("/html/body/header/div[1]/nav/ul/li[2]/a").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/a[2]").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='id_comment']")
       elem.send_keys(comment)
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='id_submit']").click()
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/a[2]").click()
       time.sleep(3)







   def tearDown(self):
        self.driver.close()