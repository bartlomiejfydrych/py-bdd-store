from selenium.webdriver.common.by import By


class LoginLocators:
#CREATE AN ACCOUNT
    EMAIL_ADDRESS_CREATE_INPUT = (By.ID, "email_create")
    CREATE_AN_ACCOUNT_BUTTON = (By.ID, "SubmitCreate")
#LOGIN
    EMAIL_ADDRESS_LOGIN_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "passwd")
    FORGOT_YOUR_PASSWORD_HREF = (By.CSS_SELECTOR, "[title='Recover your forgotten password']")
    SIGN_IN_BUTTON = (By.ID, "SubmitLogin")