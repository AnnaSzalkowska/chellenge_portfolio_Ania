import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    text_scouts_panel = "//h6[text()='Scouts Panel']"
    main_page_button = "//*[@aria-label='menu']"

    main_page_span = "//*[text()='Main page']"
    players_span = "//*[text()='Players']"
    polski_span = "//*[text()='Polski']"
    sign_out_span = "//*[text()='Sign out']"

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

    def click_on_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        time.sleep(8)
        actual_title = self.get_page_title()
        print(f"Actual Page Title: {actual_title}")
        assert actual_title.lower() == self.expected_title.lower()

    #def title_of_page(self):
    #   time.sleep(8)
    #   assert self.get_page_title() == self.expected_title


