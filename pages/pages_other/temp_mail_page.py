# Strona: https://cryptogmail.com/
import random
import string

from selenium.webdriver.support.select import Select

from locators.locators_other.temp_mail_locators import TempMailLocators
from pages.base_page import BasePage


def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class TempMailPage(TempMailLocators, BasePage):

    def go_to_temp_mail_page(self):
        self.driver.get('https://cryptogmail.com/')
        return self

    def click_change_email_button(self):
        self.find(self.CHANGE_EMAIL_BUTTON).click()

    def write_email_login(self):
        generated_mail = id_generator()
        self.find(self.EMAIL_LOGIN_INPUT).send_keys(generated_mail)

    def select_email_domain(self, index_number):
        select = Select(self.find(self.EMAIL_DOMAIN_SELECT))
        select.select_by_index(index_number)

    def click_save_email_button(self):
        self.find(self.SAVE_EMAIL_BUTTON).click()

    def get_generated_email(self):
        generated_email = self.find(self.EMAIL_GENERATED_INPUT).text
