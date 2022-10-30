from selenium.webdriver.common.by import By

from page_objects.base_element import BaseElement
from page_objects.base_page import BasePage


class DeleteEmployee(BasePage):


    def click_confirm_delete(self):
        locator = (By.XPATH, "//button[text()=' Yes, Delete ']")
        confirm_delete_element = BaseElement(driver=self.driver, locator=locator)
        confirm_delete_element.click()
        super().wait_for_successfully_saved_toast()
