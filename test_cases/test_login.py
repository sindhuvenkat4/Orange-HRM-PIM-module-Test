from page_objects.login_page import Login
from test_data.credentials import Credentials


def test_TC_Login_01(driver):
    login_page = Login(driver=driver)
    login_page.go()
    has_logged_in = login_page.input_username(username=Credentials.admin_username)\
              .input_password(password=Credentials.admin_password)\
              .click_login()\
              .has_logged_in()
    assert has_logged_in == True

def test_TC_Login_02(driver):
    login_page = Login(driver=driver)
    login_page.go()
    has_logged_in = login_page.input_username(username=Credentials.admin_username)\
              .input_password(password="Invalid password")\
              .click_login()\
              .has_logged_in()
    assert has_logged_in == False

