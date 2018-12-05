import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class groupCRUD(unittest.TestCase):

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

        # add group

        driver.get("http://127.0.0.1:8000/admin/auth/group/add/")
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Test_Group_Sel")
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(10)

        # update group

        driver.get("http://127.0.0.1:8000/admin/auth/group/")
        elem = driver.find_element_by_link_text("Test_Group_Sel")
        elem.click()
        elem = driver.find_element_by_id("id_name")
        elem.clear()
        elem.send_keys("Test_Group_Sel_update")
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(10)

        # delete group

        driver.get("http://127.0.0.1:8000/admin/auth/group/")
        elem = driver.find_element_by_link_text("Test_Group_Sel_update")
        elem.click()
        elem = driver.find_element_by_link_text("Delete")
        elem.click()
        elem = driver.find_element_by_xpath("//input[2]")
        elem.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
