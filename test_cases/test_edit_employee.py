from page_objects.login_page import Login
from test_data.credentials import Credentials


def test_TC_PIM_02(driver):
    login_page = Login(driver=driver)
    login_page.go()
    login_page.input_username(username=Credentials.admin_username) \
        .input_password(password=Credentials.admin_password) \
        .click_login() \
        .click_edit_icon("Dhuruv venkat")\
        .change_last_name("Aadhiran V")\
        .save_personal_details()
