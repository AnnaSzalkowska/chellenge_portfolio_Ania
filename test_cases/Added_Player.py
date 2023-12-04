import os
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC  # Poprawiony import
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait

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

    def test_add_new_player(self):
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
        add_match_form.click_trash_button()
        add_match_form.text_in_name_field('Marta')
        add_match_form.text_in_surname_field('Markowska')
        add_match_form.text_in_email_field('user03@getnada.com')
        add_match_form.text_in_telephone_field(329928389)
        add_match_form.text_in_age_field(12121999)
        add_match_form.click_leg_field()
        add_match_form.click_right_leg_button()
        add_match_form.text_in_main_position_field('Junior')
        add_match_form.click_submit_button()
        add_match_form.click_new_player_button()
        old_url = self.driver.current_url
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_changes(old_url))
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        add_match_form.click_new_player_button()
        expected_url = 'https://scouts-test.futbolkolektyw.pl/en/players'
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be(expected_url))

        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        time.sleep(7)
        self.driver.quit()
        time.sleep(7)
        self.driver.quit()