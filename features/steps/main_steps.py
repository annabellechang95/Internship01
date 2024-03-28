from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main(context):
    context.app.main_page.open_main()
    sleep(5)


@when('I click Menu Block button: Settings')
def click_on_settings_option(context):
    context.app.main_page.click_menu_block_button('Settings')


@then("I verify page is displayed: MainPage")
def verify_main_page(context):
    context.app.main_page.verify_main_page()


@then("I see URL contains text: {text}")
def verify_url(context, text):
    context.app.main_page.verify_page_url(text)
