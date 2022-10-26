from jproperties import Properties


class Credentials:
    config = Properties()
    with open('D:\\Code\\orange_hrm_user_creation\\configurations\\config.properties', 'rb') as config_file:
        config.load(config_file)
    admin_username = config["admin_username"].data
    admin_password = config["admin_password"].data
