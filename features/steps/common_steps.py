from behave import given, when, then


@given('open chrome browser on store site')
def step_open_store_site(context):
    context.home_page.go_to_home_page()


@then('click sign out button')
def step_click_sign_out_button(context):
    context.account_page.sign_out()
