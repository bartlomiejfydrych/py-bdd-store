from locators.account_locators import AccountLocators
from pages.base_page import BasePage


class AccountPage(AccountLocators, BasePage):

    # PANEL
    def go_to_order_history_and_details(self):
        self.find(self.ORDER_HISTORY_AND_DETAILS_BUTTON).click()

    def go_to_my_credit_slips(self):
        self.find(self.MY_CREDIT_SLIPS_BUTTON).click()

    def go_to_my_addresses(self):
        self.find(self.MY_ADDRESSES_BUTTON).click()

    def go_to_my_personal_information(self):
        self.find(self.MY_PERSONAL_INFORMATION_BUTTON).click()

    def go_to_my_wishlists(self):
        self.find(self.MY_WISHLISTS_BUTTON).click()

    # REMAINING
    def go_to_home_page(self):
        self.find(self.HOME_BUTTON).click()

    def sign_out(self):
        self.find(self.SIGN_OUT_BUTTON).click()

    def check_login_correct(self):
        assert self.find(self.MY_ACCOUNT_HEADER).is_displayed()
        assert self.find(self.MY_ACCOUNT_HEADER).text == "MY ACCOUNT"
