from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from page_objects.base_element import BaseElement
from page_objects.base_page import BasePage
from page_objects.delete_employee import DeleteEmployee
from page_objects.edit_employee import EditEmployee

class AddEmployee(BasePage):

    def has_logged_in(self):
        locator = (By.XPATH, "//p[text()='Invalid credentials']")
        try:
            BaseElement(driver=self.driver, locator=locator, should_wait=False)
            return False
        except NoSuchElementException:
            return True

    def click_add_employee(self):
        locator = (By.LINK_TEXT, "Add Employee")
        add_employee_element = BaseElement(driver=self.driver, locator=locator)
        add_employee_element.click()
        return self

    def input_first_name(self, firstname):
        locator = (By.CSS_SELECTOR, "[name='firstName']")
        first_name_element = BaseElement(driver=self.driver, locator=locator)
        first_name_element.input_text(firstname)
        return self

    def input_middle_name(self, middlename):
        locator = (By.CSS_SELECTOR, "[name='middleName']")
        middle_name_element = BaseElement(driver=self.driver, locator=locator)
        middle_name_element.input_text(middlename)
        return self

    def input_last_name(self, lastname):
        locator = (By.CSS_SELECTOR, "[name='lastName']")
        last_name_element = BaseElement(driver=self.driver, locator=locator)
        last_name_element.input_text(lastname)
        return self

    def input_employee_id(self, employee_id):
        locator = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::*/input")
        employee_id_element = BaseElement(driver=self.driver, locator=locator)
        employee_id_element.input_text(employee_id)
        return self

    def set_profile_picture(self, profile_picture_path):
        locator = (By.CSS_SELECTOR, "[type='file']")
        profile_picture_input_element = BaseElement(driver=self.driver, locator=locator, should_wait=False)
        profile_picture_input_element.input_text_without_clear(profile_picture_path)
        return self

    def click_save(self):
        locator = (By.CSS_SELECTOR, "[type='submit']")
        save_element = BaseElement(driver=self.driver, locator=locator)
        save_element.click()
        self.wait_for_successfully_saved_toast()
        self.wait_for_spinners_to_disappear()
        return self

    def input_nick_name(self, nickname):
        locator = (By.XPATH, "//label[text()='Nickname']/../following-sibling::div/input")
        nickname_element = BaseElement(driver=self.driver, locator=locator)
        nickname_element.input_text(nickname)
        return self

    def input_other_id(self, other_id):
        locator = (By.XPATH, "//label[text()='Other Id']/../following-sibling::div/input")
        other_id_element = BaseElement(driver=self.driver, locator=locator)
        other_id_element.input_text(other_id)
        return self

    def input_driver_license_number(self, driver_license_number):
        locator = (By.XPATH, "//label[text()=\"Driver's License Number\"]/../following-sibling::div/input")
        driver_license_no_element = BaseElement(driver=self.driver, locator=locator)
        driver_license_no_element.input_text(driver_license_number)
        return self

    def input_SSN_number(self, ssn_number):
        locator = (By.XPATH, "//label[text()='SSN Number']/../following-sibling::*/input")
        ssn_no_element = BaseElement(driver=self.driver, locator=locator)
        ssn_no_element.input_text(ssn_number)
        return self

    def input_SIN_number(self, sin_number):
        locator = (By.XPATH, "//label[text()='SIN Number']/../following-sibling::*/input")
        sin_no_element = BaseElement(driver=self.driver, locator=locator)
        sin_no_element.input_text(sin_number)
        return self

    def input_military_service(self, service):
        locator = (By.XPATH, "//label[text()='Military Service']/../following-sibling::*/input")
        military_service_element = BaseElement(driver=self.driver, locator=locator)
        military_service_element.input_text(service)
        return self

    def input_license_expiry_date(self, yyyy_mm_dd):
        locator = (By.XPATH, "//label[text()='License Expiry Date']/../following-sibling::*//input")
        license_expiry_date_element = BaseElement(driver=self.driver, locator=locator)
        license_expiry_date_element.input_text(yyyy_mm_dd)
        license_expiry_date_element.web_element.send_keys(Keys.TAB)
        return self

    def input_date_of_birth(self, yyyy_mm_dd):
        locator = (By.XPATH, "//label[text()='Date of Birth']/../following-sibling::*//input")
        date_of_birth_element = BaseElement(driver=self.driver, locator=locator)
        date_of_birth_element.input_text(yyyy_mm_dd)
        return self

    def select_nationality(self, nationality):
        nationlity_div_locator = (By.XPATH, "//label[text()='Nationality']/../following-sibling::*")
        nationlity_div_element = BaseElement(driver=self.driver, locator=nationlity_div_locator)
        nationlity_div_element.click()
        self.select_option(nationality)
        return self

    def select_option(self, option_text):
        dropdown_div_locator = (By.XPATH, "//div[@loading='false']/div")
        options = BaseElement(driver=self.driver, locator=dropdown_div_locator).find_elements()
        try:
            for option in options:
                if option.text == option_text:
                    option.click()
        except StaleElementReferenceException:
            print("Stale Element Reference Exception has occurred while selecting the option, " + option_text)
            # For some reason, StaleElementReferenceException is thrown, even after selecting the option.
            # Ignoring the exception for now... Need to investigate further....


    def select_marital_status(self, marital_status):
        marital_status_div_locator = (By.XPATH, "//label[text()='Marital Status']/../following-sibling::*")
        marital_status_div_element = BaseElement(driver=self.driver, locator=marital_status_div_locator)
        marital_status_div_element.click()
        self.select_option(marital_status)
        return self

    def select_blood_type(self, blood_group):
        blood_type_div_locator = (By.XPATH, "//label[text()='Blood Type']/../following-sibling::*")
        blood_type_div_element = BaseElement(driver=self.driver, locator=blood_type_div_locator)
        blood_type_div_element.click()
        self.select_option(blood_group)
        return self

    def select_gender(self, gender):
        locator = (By.XPATH, "//label[text()='" + gender + "']/span")
        element = BaseElement(driver=self.driver, locator=locator)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element.web_element)
        element.click()
        return self

    def select_smoker(self):
        locator = (By.XPATH, "//label[text()='Smoker']/../following-sibling::*")
        element = BaseElement(driver=self.driver, locator=locator)
        element.click()
        return self

    def save_personal_details(self):
        locator = (By.XPATH, "//h6[text()='Personal Details']/..//button")
        element = BaseElement(driver=self.driver, locator=locator)
        element.click()
        return self

    def save_custom_fields(self):
        locator = (By.XPATH, "//h6[text()='Custom Fields']/..//button")
        element = BaseElement(driver=self.driver, locator=locator)
        element.click()

    def click_edit_icon(self, name):
        locator = (By.XPATH, "//div[text()='" + name + "']/../../*//button/i[contains(@class,'bi-pencil-fill')]")
        edit_icon_element = BaseElement(driver=self.driver, locator=locator)
        edit_icon_element.click()
        return EditEmployee(driver=self.driver)

    def click_delete_icon(self, name):
        locator = (By.XPATH, "//div[text()='" + name + "']/../../*//button/i[contains(@class,'bi-trash')]")
        delete_icon_element = BaseElement(driver=self.driver, locator=locator)
        delete_icon_element.click()
        return DeleteEmployee(driver=self.driver)




















