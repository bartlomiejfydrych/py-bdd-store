from behave import given, when, then

mail_login = "abc001.test0001@gmail.com"
password_login = "123store"


@when('click on sign in button')
def step_click_sign_in_button(context):
    context.login_page = context.home_page.go_to_login()


@when('write login email address')
def step_write_login_email_address(context):
    context.login_page.write_email_login(mail_login)


@when('write login password')
def step_write_login_password(context):
    context.login_page.write_password(password_login)


@when('click login sign in button')
def step_click_login_sign_in_button(context):
    context.account_page = context.login_page.click_sign_in()


@then('user logged successfully')
def step_check_user_logged_successfully(context):
    context.account_page.check_login_correct()