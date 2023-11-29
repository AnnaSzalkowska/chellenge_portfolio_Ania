import os
import unittest

from selenium import webdriver
from selenium.common import WebDriverException

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_a_match_form import AddaMatchForm
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class AddaPlayer(unittest.TestCase):
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
        dashboard_page.click_add_player_button()
        add_match_form = AddaMatchForm(self.driver)
        add_match_form.click_add_language_button()
        add_match_form.type_in_language('Polish')
        add_match_form.click_add_language_button()

        max_clicks = 0  # Initialize max_clicks before entering the loop

        try:
            while True:
                add_match_form.click_add_language_button()
                max_clicks += 1
        except WebDriverException:
            # Exception occurred, break out of the loop

            # Print or assert the result
            print(f"Maximum number of successful clicks: {max_clicks}")

        # Continue with the rest of your test logic...
