import random

from page_objects.login_page import Login
from test_data.credentials import Credentials
from pathlib import Path


def test_TC_PIM_01(driver):
    login_page = Login(driver=driver)
    login_page.go()
    login_page.input_username(username=Credentials.admin_username) \
              .input_password(password=Credentials.admin_password) \
              .click_login() \
              .click_add_employee()\
    .input_first_name("Dhuruv")\
    .input_middle_name("venkat")\
    .input_last_name("Aadhiran")\
    .input_employee_id(random.randint(100000,999999))\
    .set_profile_picture(str(Path("../test_data/images.jpg").resolve().absolute()))\
    .click_save()\
    .input_other_id("8907")\
    .input_driver_license_number("87839393")\
    .input_license_expiry_date("2022-11-12")\
    .input_date_of_birth("1992-08-04")\
    .select_nationality("Indian")\
    .select_marital_status("Single")\
    .select_blood_type("O+")\
    .select_gender("Male")\
    .save_personal_details()\
    .save_custom_fields()






