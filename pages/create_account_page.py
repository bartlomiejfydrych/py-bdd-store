from selenium.webdriver.support.select import Select

from locators.create_account_locators import CreateAccountLocators
from pages.base_page import BasePage


class CreateAccountPage(CreateAccountLocators, BasePage):

    # YOUR PERSONAL INFORMATION
    # Title
    def select_title(self, title):
        if title == "Mr.":
            self.find(self.MR_RADIO).click()
        elif title == "Mrs.":
            self.find(self.MRS_RADIO).click()
        else:
            print("Incorrect title")

    def write_first_name(self, first_name):
        self.find(self.FIRST_NAME_INPUT).send_keys(first_name)

    def write_last_name(self, last_name):
        self.find(self.LAST_NAME_INPUT).send_keys(last_name)

    def write_password(self, password):
        self.find(self.PASSWORD_INPUT).send_keys(password)

    # Date of Birth selects
    def select_day_of_birth(self, day):
        select = Select(self.find(self.DAY_SELECT))
        select.select_by_visible_text(day)

    def select_month_of_birth(self, month):
        select = Select(self.find(self.MONTH_SELECT))
        select.select_by_visible_text(month)

    def select_year_of_birth(self, year):
        select = Select(self.find(self.YEAR_SELECT))
        select.select_by_visible_text(year)

    # YOUR ADDRESS
    def write_company(self, company):
        self.find(self.COMPANY_INPUT).send_keys(company)

    def write_address(self, address_1):
        self.find(self.ADDRESS_1_INPUT).send_keys(address_1)

    def write_address_2(self, address_2):
        self.find(self.ADDRESS_2_INPUT).send_keys(address_2)

    def write_city(self, city):
        self.find(self.CITY_INPUT).send_keys(city)

    def select_state(self, state):
        select = Select(self.find(self.STATE_SELECT))
        select.select_by_visible_text(state)

    def write_postal_code(self, postal_code):
        self.find(self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def select_country(self, country):
        select = Select(self.find(self.COUNTRY_SELECT))
        select.select_by_visible_text(country)

    def write_additional_information(self, additional_information):
        self.find(self.ADDITIONAL_INFORMATION_INPUT).send_keys(additional_information)

    def write_home_phone_number(self, home_number):
        self.find(self.HOME_PHONE_INPUT).send_keys(home_number)

    def write_mobile_phone_number(self, mobile_number):
        self.find(self.MOBILE_PHONE_INPUT).send_keys(mobile_number)

    def write_address_alias(self, address_alias):
        self.find(self.ADDRESS_ALIAS_INPUT).send_keys(address_alias)

    # REGISTER BUTTON
    def click_register_button(self):
        self.find(self.REGISTER_BUTTON).click()
