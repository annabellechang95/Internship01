from behave import given, when, then


@given('I navigate to: https://soft.reelly.io/sign-in')
def open_google(context):
    context.app.sign_in_page.open_sign_in_page()


@when('I input username: {username}')
def input_username(context, username):
    context.app.sign_in_page.input_username(username)


@when('I input password: {password}')
def input_password(context, password):
    context.app.sign_in_page.input_password(password)


@when('I click button: Continue')
def click_continue_button(context):
    context.app.sign_in_page.click_continue_button()
