import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class productCRUD(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_group(self):

        # admin login

        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(5)

        # create category

        driver.get("http://127.0.0.1:8000/admin/shop/category/add/")
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Games_Sel")
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(5)

        # create product

        driver.get("http://127.0.0.1:8000/admin/shop/product/")
        time.sleep(3)
        driver.get("http://127.0.0.1:8000/admin/shop/product/add/")
        elem = driver.find_element_by_xpath("//select[@id='id_category']/option[2]")
        elem.click()
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Game_Sel")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Test Game")
        elem = driver.find_element_by_id("id_price")
        elem.send_keys("60.00")
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(5)

        # update category

        driver.get("http://127.0.0.1:8000/admin/shop/category/")
        elem = driver.find_element_by_link_text("Games_Sel")
        elem.click()
        elem = driver.find_element_by_id("id_name")
        elem.clear()
        elem.send_keys("Games_Sel_update")
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(5)

        # update game

        driver.get("http://127.0.0.1:8000/admin/shop/product/")
        elem = driver.find_element_by_link_text("Game_Sel")
        elem.click()
        elem = driver.find_element_by_id("id_name")
        elem.clear()
        elem.send_keys("Game_Sel_update")
        elem = driver.find_element_by_id("id_description")
        elem.clear()
        elem.send_keys("Test Game Update")
        elem = driver.find_element_by_id("id_price")
        elem.clear()
        elem.send_keys("30.00")
        elem = driver.find_element_by_id("id_slug")
        elem.clear()
        elem.send_keys("game_sel_update")
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(5)

        # delete game

        driver.get("http://127.0.0.1:8000/admin/shop/product/")
        elem = driver.find_element_by_link_text("Game_Sel_update")
        elem.click()
        elem = driver.find_element_by_link_text("Delete")
        elem.click()
        elem = driver.find_element_by_xpath("//input[2]")
        elem.click()
        time.sleep(5)

        # delete category

        driver.get("http://127.0.0.1:8000/admin/shop/category/")
        elem = driver.find_element_by_link_text("Games_Sel_update")
        elem.click()
        elem = driver.find_element_by_link_text("Delete")
        elem.click()
        elem = driver.find_element_by_xpath("//input[2]")
        elem.click()
        time.sleep(5)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
