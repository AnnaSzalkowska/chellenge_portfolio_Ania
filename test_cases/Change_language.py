import os
import time
import unittest

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestSignOut(unittest.TestCase):
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_change_language_to_polish(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.check_title_of_page()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        old_url = self.driver.current_url
        dashboard_page.click_change_language_button()
        dashboard_page.wait_for_url_change(old_url)
        dashboard_page.text_in_polish()
        self.driver.quit()
