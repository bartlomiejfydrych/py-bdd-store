from locators.login_locators import LoginLocators
from pages.account_page import AccountPage
from pages.base_page import BasePage


class LoginPage(LoginLocators, BasePage):

#CREATE AN ACCOUNT
    def write_email_create(self, email):
        self.find(self.EMAIL_ADDRESS_CREATE_INPUT).send_keys(email)

    def click_create_account(self):
        self.find(self.CREATE_AN_ACCOUNT_BUTTON).click()

#LOGIN
    def write_email_login(self, email):
        self.find(self.EMAIL_ADDRESS_LOGIN_INPUT).send_keys(email)

    def write_password(self, password):
        self.find(self.PASSWORD_INPUT).send_keys(password)

    def click_sign_in(self):
        self.find(self.SIGN_IN_BUTTON).click()
        return AccountPage(self.driver)