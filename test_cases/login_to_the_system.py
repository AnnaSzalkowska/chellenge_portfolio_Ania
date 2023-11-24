import os
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()

        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://scouts-test.futbolkolektyw.pl/login')

    def test_assert_element_text(self):
        xpath = "//*[text()='Scouts Panel']"
        expected_text = "Scouts Panel"

        element = self.driver.find_element(By.XPATH, xpath)
        element_text = element.text

        assert expected_text == element_text, f"Expected text: {expected_text}, Actual text: {element_text}"
