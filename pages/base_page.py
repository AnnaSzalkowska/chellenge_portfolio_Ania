from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE


def assert_element_text(driver, xpath, expected_text):
    """Comparing expected text with observed value from web element

        :param driver: webdriver instance
        :param xpath: xpath to element with text to be observed
        :param expected_text: text what we expecting to be found
        :return: None
    """
    element = driver.find_element(by=By.XPATH, value=xpath)
    element_text = element.text
    assert expected_text == element_text


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self):
        return self.driver.title

    def find_element_by_xpath(self, xpath):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


