from behave import given, when, then
from pages import home_page

from pages.home_page import HomePage
from pages.contact_page import ContactPage

option_select = 'Customer service'
email = 'innbart92@gmail.com'
order = '123'
text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam et congue justo. Aliquam a neque.'


@when('click on contact us button')
def step_click_contact(context):
    context.contact_page = context.home_page.go_to_contact_us()


@when('choose subject heading')
def step_choose_subject(context):
    context.contact_page.subject_choose(option_select)


@when('write email address')
def step_write_email(context):
    context.contact_page.email_write(email)


@when('write order reference')
def step_write_order_reference(context):
    context.contact_page.order_write(order)


@when('attach file')
def step_attach_file(context):
    context.contact_page.attach_file()


@when('write message')
def step_write_message(context):
    context.contact_page.message_write(text)


@when('click send button')
def step_click_send(context):
    context.contact_page.send_button_click()


@then('mail send successfully')
def step_check_alert(context):
    context.contact_page.check_alert()
