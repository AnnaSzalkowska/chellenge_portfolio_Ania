import os
import unittest
from selenium import webdriver
import time

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class AddaPlayer(unittest.TestCase):
    driver = None
    add_player_button_xpath = "//*[text()='Add player']"
    expected_title = "Scouts Panel"
    page_title = 'https://scouts-test.futbolkolektyw.pl/en'

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
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_player_button()
        time.sleep(5)
