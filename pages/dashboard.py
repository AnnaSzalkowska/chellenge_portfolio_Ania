import time

from pages.base_page import BasePage


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

    def title_of_page(self):
        test_title = "Scouts Panel"
        assert test_title == self.expected_title

    def click_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)
