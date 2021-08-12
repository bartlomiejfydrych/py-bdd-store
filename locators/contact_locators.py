from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


class ContactLocators:
    SUBJECT_SELECT = (By.ID, "id_contact")
    EMAIL_INPUT = (By.ID, "email")
    ORDER_INPUT = (By.ID, "id_order")
    ATTACH_FILE = (By.ID, "fileUpload")
    MESSAGE_INPUT = (By.ID, "message")
    SEND_BUTTON = (By.ID, "submitMessage")
    SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")
