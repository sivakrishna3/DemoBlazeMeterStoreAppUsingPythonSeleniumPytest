import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_base_url():
        base_url = config.get('Login_info', 'base_url')
        return base_url

    @staticmethod
    def get_username():
        username = config.get('Login_info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('Login_info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('Login_info', 'invalid_username')
        return invalid_username

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('Login_info', 'invalid_password')
        return invalid_password

    @staticmethod
    def get_username_with_numbers():
        username_with_numbers = config.get("Login_info", "username_with_numbers")
        return username_with_numbers

    @staticmethod
    def get_password_with_numbers():
        password_with_numbers = config.get("Login_info", "password_with_numbers")
        return password_with_numbers

    @staticmethod
    def get_no_username():
        no_username = config.get('Login_info', 'no_username')
        return no_username

    @staticmethod
    def get_no_password():
        no_password = config.get('Login_info', 'no_password')
        return no_password

    @staticmethod
    def get_username_with_spl_chars():
        username_with_spl_chars = config.get('Login_info', 'username_with_spl_chars')
        return username_with_spl_chars

    @staticmethod
    def get_password_with_spl_chars():
        password_with_spl_chars = config.get('Login_info', 'password_with_spl_chars')
        return password_with_spl_chars

    @staticmethod
    def get_username_with_space():
        username_with_space = config.get('Login_info', 'username_with_space')
        return username_with_space

    @staticmethod
    def get_password_with_space():
        password_with_space = config.get('Login_info', 'password_with_space')
        return password_with_space

    @staticmethod
    def get_contact_email():
        contact_email = config.get("Contact_page_info", "email_text")
        return contact_email

    @staticmethod
    def get_contact_invalid_email():
        contact_invalid_email = config.get("Contact_page_info", "invalid_email_text")
        return contact_invalid_email

    @staticmethod
    def get_contact_empty_email():
        contact_empty_email = config.get("Contact_page_info", "empty_email_text")
        return contact_empty_email

    @staticmethod
    def get_contact_email_with_spl_chars():
        contact_email_with_spl_chars = config.get("Contact_page_info", "Contact_page_info")

    @staticmethod
    def get_contact_name():
        contact_name = config.get("Contact_page_info", "name_text")
        return contact_name

    @staticmethod
    def get_contact_invalid_name():
        contact_invalid_name = config.get("Contact_page_info", "invalid_name_text")
        return contact_invalid_name

    @staticmethod
    def get_contact_empty_name():
        contact_empty_name = config.get("Contact_page_info", "empty_name_text")
        return contact_empty_name

    @staticmethod
    def get_contact_message():
        contact_message = config.get("Contact_page_info", "message_text")
        return contact_message

    @staticmethod
    def get_contact_invalid_message():
        contact_invalid_message = config.get("Contact_page_info", "invalid_message_text")
        return contact_invalid_message

    @staticmethod
    def get_contact_empty_message():
        contact_empty_message = config.get("Contact_page_info", "empty_message_text")
        return contact_empty_message

    @staticmethod
    def get_cart_name():
        cart_name = config.get("Cart_info", "name")
        return cart_name

    @staticmethod
    def get_cart_no_name():
        cart_no_name = config.get("Cart_info", "no_name")
        return cart_no_name

    @staticmethod
    def get_cart_country():
        cart_country = config.get("Cart_info", "country")
        return cart_country

    @staticmethod
    def get_cart_no_country():
        cart_no_country = config.get("Cart_info", "no_country")
        return cart_no_country

    @staticmethod
    def get_cart_city():
        cart_city = config.get("Cart_info", "city")
        return cart_city

    @staticmethod
    def get_cart_no_city():
        cart_no_city = config.get("Cart_info", "no_city")
        return cart_no_city

    @staticmethod
    def get_cart_credit_card():
        cart_credit_card = config.get("Cart_info", "credit_card")
        return cart_credit_card

    @staticmethod
    def get_cart_no_credit_card():
        cart_no_credit_card = config.get("Cart_info", "no_credit_card")
        return cart_no_credit_card

    @staticmethod
    def get_cart_month():
        cart_month = config.get("Cart_info", "month")
        return cart_month

    @staticmethod
    def get_cart_no_month():
        cart_no_month = config.get("Cart_info", "no_month")
        return cart_no_month

    @staticmethod
    def get_cart_year():
        cart_year = config.get("Cart_info", "year")
        return cart_year

    @staticmethod
    def get_cart_no_year():
        cart_no_year = config.get("Cart_info", "no_year")
        return cart_no_year
