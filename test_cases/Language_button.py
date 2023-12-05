import os
import unittest

from selenium import webdriver
from selenium.common import WebDriverException

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_a_match_form import AddaMatchForm
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLanguageButton(unittest.TestCase):
    driver = None
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_language_button(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_player_button()
        add_match_form = AddaMatchForm(self.driver)
        add_match_form.click_add_language_button()
        add_match_form.type_in_language('Polish')
        add_match_form.click_add_language_button()

        max_clicks = 30
        current_clicks = 0

        try:
            while current_clicks < max_clicks:
                add_match_form.click_add_language_button()
                current_clicks += 1
        except WebDriverException:
            print(f"Maximum number of successful clicks: {current_clicks}")
            self.fail("Test failed. Maximum number of clicks reached.")

    if __name__ == '__main__':
        unittest.main()