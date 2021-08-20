from selenium.webdriver.common.by import By


class AccountLocators:
#HEADER
    MY_ACCOUNT_HEADER = (By.CLASS_NAME, "page-heading")
#PANEL
    ORDER_HISTORY_AND_DETAILS_BUTTON = (By.CSS_SELECTOR, "[title='Orders']")
    MY_CREDIT_SLIPS_BUTTON = (By.CSS_SELECTOR, "[title='Credit slips']")
    MY_ADDRESSES_BUTTON = (By.CSS_SELECTOR, "[title='Addresses']")
    MY_PERSONAL_INFORMATION_BUTTON = (By.CSS_SELECTOR, "[title='Information']")
    MY_WISHLISTS_BUTTON = (By.CSS_SELECTOR, "[title='My wishlists']")
#REMAINING
    HOME_BUTTON = (By.CSS_SELECTOR, "[title='Home']")
    SIGN_OUT_BUTTON = (By.CLASS_NAME, "logout")