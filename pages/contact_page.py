from selenium.webdriver.support.select import Select

from files_configuration import PICTURE_PATH
from locators.contact_locators import ContactLocators
from pages.base_page import BasePage

class ContactPage(ContactLocators, BasePage):

    def subject_choose(self, option_select):
        select = Select(self.find(self.SUBJECT_SELECT))
        select.select_by_visible_text(option_select)
    
    def email_write(self, email):
        self.find(self.EMAIL_INPUT).send_keys(email)
    
    def order_write(self, order):
        self.find(self.ORDER_INPUT).send_keys(order)
    
    def attach_file(self):
        self.find(self.ATTACH_FILE).send_keys(PICTURE_PATH)
    
    def message_write(self, text):
        self.find(self.MESSAGE_INPUT).send_keys(text)
    
    def send_button_click(self):
        self.find(self.SEND_BUTTON).click()
    
    def check_alert(self):
        assert self.find(self.SUCCESS_ALERT).is_displayed()
        assert self.find(self.SUCCESS_ALERT).getText() == "Your message has been successfully sent to our team."