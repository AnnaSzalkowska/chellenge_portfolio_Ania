from pages.base_page import BasePage, assert_element_text


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts-test.futbolkolektyw.pl/login"
    header_page_title_xpath = "//*[text()='Scouts Panel']"
    expected_header = "Scouts Panel"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_the_page(self):
        self.get_page_title()
        assert self.expected_title == self.get_page_title()

    def check_title_of_page(self):
        assert_element_text(self.driver, self.header_page_title_xpath, self.expected_header)

