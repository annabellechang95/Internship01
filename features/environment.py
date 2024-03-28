from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()

    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)

    print('\nStarted step: ', step.name)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

        # context.driver.save_screenshot(f"{step.name}_test.png")
        print('\nStep failed: ', step.name)

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()