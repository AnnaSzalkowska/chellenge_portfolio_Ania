from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddaMatchForm(BasePage):
    submit_label = "//*[text()='Submit']"
    clear_button = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]"
    clear_label = "//*[text()='Clear']"
    title = "/*[@id='__next']/div[1]/main/div[2]/form/div[1]"
    title_text = "//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span"
    match_at_home_label = "//*[text()='Match at home']"
    match_out_home_label = "//*[text()='Match out home']"
    match_fieldset = "//fieldset"
    date_text = "//*[text()='Date']"
    error_paragraph = "//p[text()='Required']"
    text_scouts_panel = "//h6[text()='Scouts Panel']"
    add_language_button_xpath = "//*[text()='Add language']"
    time_played_grid = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]"
    number_grid = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]"
    web_math_grid = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]"
    languages_label_xpath = '//*[@name ="languages[0]"]'
    trash_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[15]/div[2]/button/span[1]'
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    email_field_xpath = "//*[@name='email']"
    telephone_field_xpath = "//*[@name='phone']"
    age_field_xpath = "//*[@name='age']"
    leg_field_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_button_xpath = "//*[text()= 'Right leg']"
    main_position_field_xpath = "//*[@name= 'mainPosition']"
    submit_button_xpath = "//*[text()= 'Submit']"
    new_player_button_xpath = "//*[text() = 'Players']"


    def click_add_language_button(self):
        self.click_on_the_element(self.add_language_button_xpath)

    def type_in_language(self, language):
        self.field_send_keys(self.languages_label_xpath, language)

    def click_trash_button(self):
        self.click_on_the_element(self.trash_xpath)

    def text_in_name_field(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def text_in_surname_field(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def text_in_email_field(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def text_in_telephone_field(self, phone):
        self.field_send_keys(self.telephone_field_xpath, phone)

    def text_in_age_field(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def click_leg_field(self):
        self.click_on_the_element(self.leg_field_xpath)

    def click_right_leg_button(self):
        self.click_on_the_element(self.right_leg_button_xpath)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def text_in_main_position_field(self, position):
        self.field_send_keys(self.main_position_field_xpath, position)

    def click_new_player_button(self):
        self.click_on_the_element(self.new_player_button_xpath)
