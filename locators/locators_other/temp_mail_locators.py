from selenium.webdriver.common.by import By


# Strona: https://cryptogmail.com/

class TempMailLocators:
    CHANGE_EMAIL_BUTTON = (By.CLASS_NAME, "button--change")
    EMAIL_LOGIN_INPUT = (By.CLASS_NAME, "new-email--address")
    EMAIL_DOMAIN_SELECT = (By.CLASS_NAME, "new-email__select-options")
    SAVE_EMAIL_BUTTON = (By.CLASS_NAME, "button--change-email")
    EMAIL_GENERATED_INPUT = (By.CLASS_NAME, "field--value")
