from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage

def before_feature(context, feature):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()
    context.home_page = HomePage(context.driver)

def after_feature(context, feature):
    context.driver.quit()