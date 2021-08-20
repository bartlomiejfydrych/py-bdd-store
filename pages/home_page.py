from locators.home_locators import HomeLocators

from pages.base_page import BasePage
from pages.contact_page import ContactPage
from pages.login_page import LoginPage


class HomePage(HomeLocators, BasePage):

    # GO TO methods:
    def go_to_home_page(self):
        self.driver.get('http://automationpractice.com/index.php')
        return self

    def go_to_contact_us(self):
        self.find(self.CONTACT_US_BUTTON).click()
        return ContactPage(self.driver)

    def go_to_login(self):
        self.find(self.SIGN_IN_BUTTON).click()
        return LoginPage(self.driver)