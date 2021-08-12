from behave import given, when, then


@given('open chrome browser on store site')
def step_open_store_site(context):
    context.home_page.go_to_home_page()
