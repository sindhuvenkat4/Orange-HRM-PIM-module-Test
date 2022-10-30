from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_element import BaseElement


class BasePage:

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def wait_until(self, condition, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(condition)

    def wait_for_successfully_saved_toast(self):
        locator = (By.CSS_SELECTOR, ".oxd-toast-content--success")
        toast_success_element = BaseElement(driver=self.driver, locator=locator).web_element
        self.wait_until(EC.invisibility_of_element(toast_success_element))

    def wait_for_spinners_to_disappear(self):
        locator = (By.CSS_SELECTOR, ".oxd-loading-spinner")
        spinner_element = BaseElement(driver=self.driver, locator=locator).web_element
        self.wait_until(EC.invisibility_of_element(spinner_element))
