import time

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Dashboard(BasePage):
    text_scouts_panel = "//h6[text()='Scouts Panel']"
    main_page_button = "//*[@aria-label='menu']"

    main_page_span = "//*[text()='Main page']"
    players_span = "//*[text()='Players']"
    polski_span = "//*[text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"

    logo_scouts_panel = "//*[@title='Logo Scouts Panel']"
    contact_label = "//*[text()='Dev team contact']"
    scotus_panel_paragraph = "//p[text()='Player, match and report management panel.']"
    text_shortcuts = "//h2[text()='Shortcuts']"
    add_player_label = "//*[text()='Add player']"

    text_activity = "//h2[text()='Activity']"
    text_last_created_player = "//h6[text()='Last created player']"
    text_last_updated_player = "//h6[text()='Last updated player']"

    login_url = "https://scouts-test.futbolkolektyw.pl/login"
    Dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    add_player_button_xpath = "//*[text()='Add player']"
    expected_title = "Scouts Panel"
    add_language_xpath = "//*[text()='Add language']"
    change_language_to_polish_xpath = "//*[text() = 'Polski']"
    text_in_polish_xpath = "//*[text() = 'Linki pomocnicze']"
    expected_text = 'Linki pomocnicze'

    def title_of_page(self):
        test_title = "Scouts Panel"
        assert test_title == self.expected_title

    def click_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_change_language_button(self):
        self.click_on_the_element((self.change_language_to_polish_xpath))

    def get_text_from_element(self, xpath):
        element = self.find_element_by_xpath(xpath)
        return element.text if element else None

    def wait_for_url_change(self, old_url):
        timeout = 10
        WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))

    def text_in_polish(self):
        actual_text = self.get_text_from_element(self.text_in_polish_xpath)
        assert actual_text == self.expected_text, f"Expected text: {self.expected_text}, Actual text: {actual_text}"
