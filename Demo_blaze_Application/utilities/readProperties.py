import configparser
import json
import os
# import sys

ini_file_path = ".\\Configurations\\config.ini"
try:
    if not os.path.exists(ini_file_path):
        print("File not exist, provide the file: " + ini_file_path)
    config = configparser.RawConfigParser()
    config.read(ini_file_path)
except FileNotFoundError:
    print("Please provide the ini file path.")


class ReadConfig:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_json_data():
        try:
            json_file_path = "./Locators/locators.json"
            with open(json_file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError as e:
            print(f"{e} : Please provide the json file path.")

    @staticmethod
    def get_base_url():
        try:
            base_url = config.get('Login_info', 'base_url')
            return base_url
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_username():
        try:
            username = config.get('Login_info', 'username')
            return username
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_password():
        try:
            password = config.get('Login_info', 'password')
            return password
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_invalid_username():
        try:
            invalid_username = config.get('Login_info', 'invalid_username')
            return invalid_username
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_invalid_password():
        try:
            invalid_password = config.get('Login_info', 'invalid_password')
            return invalid_password
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_username_with_numbers():
        try:
            username_with_numbers = config.get("Login_info", "username_with_numbers")
            return username_with_numbers
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_password_with_numbers():
        try:
            password_with_numbers = config.get("Login_info", "password_with_numbers")
            return password_with_numbers
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_no_username():
        try:
            no_username = config.get('Login_info', 'no_username')
            return no_username
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_no_password():
        try:
            no_password = config.get('Login_info', 'no_password')
            return no_password
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_username_with_spl_chars():
        try:
            username_with_spl_chars = config.get('Login_info', 'username_with_spl_chars')
            return username_with_spl_chars
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_password_with_spl_chars():
        try:
            password_with_spl_chars = config.get('Login_info', 'password_with_spl_chars')
            return password_with_spl_chars
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_username_with_space():
        try:
            username_with_space = config.get('Login_info', 'username_with_space')
            return username_with_space
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_password_with_space():
        try:
            password_with_space = config.get('Login_info', 'password_with_space')
            return password_with_space
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_contact_email():
        try:
            contact_email = config.get("Contact_page_info", "email_text")
            return contact_email
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_contact_invalid_email():
        try:
            contact_invalid_email = config.get("Contact_page_info", "invalid_email_text")
            return contact_invalid_email
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_contact_empty_email():
        try:
            contact_empty_email = config.get("Contact_page_info", "empty_email_text")
            return contact_empty_email
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_contact_email_with_spl_chars():
        try:
            contact_email_with_spl_chars = config.get("Contact_page_info", "email_with_spl_chars")
            return contact_email_with_spl_chars
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_contact_name():
        try:
            contact_name = config.get("Contact_page_info", "name_text")
            return contact_name
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_contact_invalid_name():
        try:
            contact_invalid_name = config.get("Contact_page_info", "invalid_name_text")
            return contact_invalid_name
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_contact_empty_name():
        try:
            contact_empty_name = config.get("Contact_page_info", "empty_name_text")
            return contact_empty_name
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_contact_message():
        try:
            contact_message = config.get("Contact_page_info", "message_text")
            return contact_message
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_contact_invalid_message():
        try:
            contact_invalid_message = config.get("Contact_page_info", "invalid_message_text")
            return contact_invalid_message
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_contact_empty_message():
        try:
            contact_empty_message = config.get("Contact_page_info", "empty_message_text")
            return contact_empty_message
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_name():
        try:
            cart_name = config.get("Cart_info", "name")
            return cart_name
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_no_name():
        try:
            cart_no_name = config.get("Cart_info", "no_name")
            return cart_no_name
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_country():
        try:
            cart_country = config.get("Cart_info", "country")
            return cart_country
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_no_country():
        try:
            cart_no_country = config.get("Cart_info", "no_country")
            return cart_no_country
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_city():
        try:
            cart_city = config.get("Cart_info", "city")
            return cart_city
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_no_city():
        try:
            cart_no_city = config.get("Cart_info", "no_city")
            return cart_no_city
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_credit_card():
        try:
            cart_credit_card = config.get("Cart_info", "credit_card")
            return cart_credit_card
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_no_credit_card():
        try:
            cart_no_credit_card = config.get("Cart_info", "no_credit_card")
            return cart_no_credit_card
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_month():
        try:
            cart_month = config.get("Cart_info", "month")
            return cart_month
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_no_month():
        try:
            cart_no_month = config.get("Cart_info", "no_month")
            return cart_no_month
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_year():
        try:
            cart_year = config.get("Cart_info", "year")
            return cart_year
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_cart_no_year():
        try:
            cart_no_year = config.get("Cart_info", "no_year")
            return cart_no_year
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_username():
        username = config.get('Sign_up_info', 'sg_username')
        return username

    @staticmethod
    def get_sign_up_password():
        try:
            password = config.get('Sign_up_info', 'sg_password')
            return password
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_invalid_username():
        try:
            invalid_username = config.get('Sign_up_info', 'invalid_username')
            return invalid_username
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_invalid_password():
        try:
            invalid_password = config.get('Sign_up_info', 'invalid_password')
            return invalid_password
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_username_with_numbers():
        try:
            username_with_numbers = config.get("Sign_up_info", "username_with_numbers")
            return username_with_numbers
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_password_with_numbers():
        try:
            password_with_numbers = config.get("Sign_up_info", "password_with_numbers")
            return password_with_numbers
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_no_username():
        try:
            no_username = config.get('Sign_up_info', 'no_username')
            return no_username
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_no_password():
        try:
            no_password = config.get('Sign_up_info', 'no_password')
            return no_password
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_username_with_spl_chars():
        try:
            username_with_spl_chars = config.get('Sign_up_info', 'username_with_spl_chars')
            return username_with_spl_chars
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_password_with_spl_chars():
        try:
            password_with_spl_chars = config.get('Sign_up_info', 'password_with_spl_chars')
            return password_with_spl_chars
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_username_with_space():
        try:
            username_with_space = config.get('Sign_up_info', 'username_with_space')
            return username_with_space
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

    @staticmethod
    def get_sign_up_password_with_space():
        try:
            password_with_space = config.get('Sign_up_info', 'password_with_space')
            return password_with_space
        except (configparser.NoSectionError, configparser.NoOptionError) as error:
            print(f"{error} : Field is missing, Please check the ini file")

