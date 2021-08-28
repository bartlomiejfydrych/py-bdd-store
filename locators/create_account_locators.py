from selenium.webdriver.common.by import By


class CreateAccountLocators:
    # YOUR PERSONAL INFORMATION
    # Title
    MR_RADIO = (By.ID, "uniform-id_gender1")
    MRS_RADIO = (By.ID, "uniform-id_gender2")

    FIRST_NAME_INPUT = (By.ID, "customer_firstname")
    LAST_NAME_INPUT = (By.ID, "customer_lastname")
    PASSWORD_INPUT = (By.ID, "passwd")

    # Date of Birth selects
    DAY_SELECT = (By.ID, "days")
    MONTH_SELECT = (By.ID, "months")
    YEAR_SELECT = (By.ID, "years")

    # YOUR ADDRESS
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS_1_INPUT = (By.ID, "address1")
    ADDRESS_2_INPUT = (By.ID, "address2")
    CITY_INPUT = (By.ID, "city")
    STATE_SELECT = (By.ID, "id_state")
    POSTAL_CODE_INPUT = (By.ID, "postcode")
    COUNTRY_SELECT = (By.ID, "id_country")
    ADDITIONAL_INFORMATION_INPUT = (By.ID, "other")
    HOME_PHONE_INPUT = (By.ID, "phone")
    MOBILE_PHONE_INPUT = (By.ID, "phone_mobile")
    ADDRESS_ALIAS_INPUT = (By.ID, "alias")

    # REGISTER BUTTON
    REGISTER_BUTTON = (By.ID, "submitAccount")
