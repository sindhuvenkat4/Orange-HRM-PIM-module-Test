from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseElement:

    def __init__(self, driver, locator, should_wait=True, timeout=10):
        self.driver = driver
        self.locator = locator
        self.should_wait = should_wait

        self.wait = WebDriverWait(self.driver, timeout)
        self.web_element = None
        self.find_element()

    def find_elements(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator=self.locator))
        return elements

    def find_element(self):
        if self.should_wait:
            element = self.wait.until(EC.visibility_of_element_located(locator=self.locator))
            self.web_element = element
        else:
            element = self.driver.find_element(*self.locator)
            self.web_element = element

    def find_element_within_element(self, locator):
        return self.web_element.find_element(*locator)

    def clear_text(self):
        self.click()
        self.web_element.clear()
        return None

    def input_text(self, text):
        self.clear_text()
        self.input_text_without_clear(text)
        return None

    def input_text_without_clear(self, text):
        self.web_element.send_keys(text)
        return None

    def click(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(mark=self.web_element))
            element.click()
        except ElementClickInterceptedException:
            element = self.wait.until(EC.element_to_be_clickable(mark=self.web_element))
            element.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text

    @property
    def displayed(self):
        return self.web_element.is_displayed()




