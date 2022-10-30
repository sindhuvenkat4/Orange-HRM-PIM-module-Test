from selenium.webdriver.common.by import By

from page_objects.base_element import BaseElement
from page_objects.base_page import BasePage
from page_objects.delete_employee import DeleteEmployee


class EditEmployee(BasePage):
    def change_last_name(self, new_last_name):
        locator = (By.CSS_SELECTOR, "[name='lastName']")
        super().wait_for_spinners_to_disappear()
        last_name_element = BaseElement(driver=self.driver, locator=locator)
        last_name_element.input_text(new_last_name)
        return self

    def save_personal_details(self):
        locator = (By.XPATH, "//h6[text()='Personal Details']/..//button")
        element = BaseElement(driver=self.driver, locator=locator)
        element.click()
        super().wait_for_successfully_saved_toast()





