from webdriver_manager.chrome import ChromeDriverManager
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from page_objects.base_element import BaseElement
from page_objects.add_employee import AddEmployee


class Login(BasePage):

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def input_username(self, username):
        locator = (By.CSS_SELECTOR, "[name='username']")
        username_element = BaseElement(driver=self.driver, locator=locator)
        username_element.clear_text()
        username_element.input_text(username)
        return self

    def input_password(self, password):
        locator = (By.CSS_SELECTOR, "[name='password']")
        password_element = BaseElement(driver=self.driver, locator=locator)
        password_element.input_text(password)
        return self

    def click_login(self):
        locator = (By.CSS_SELECTOR, "[type='submit']")
        login_element = BaseElement(driver=self.driver, locator=locator)
        login_element.click()
        return AddEmployee(driver=self.driver)




